import Foundation
import XCTest
@testable import StarterCore

final class StarterCoreTests: XCTestCase {
    func testNormalizeWhitespacePreservesTextAndDeclaresLineCollapse() {
        XCTAssertEqual(TextTools.normalizedWhitespace("  một\t hai\n👩🏽‍💻  "), "một hai 👩🏽‍💻")
        XCTAssertEqual(TextTools.normalizedWhitespace("\n\t "), "")
    }

    func testStatisticsHaveExplicitEmptyUnicodeAndLineSemantics() {
        XCTAssertEqual(TextTools.statistics(""), TextStatistics(characters: 0, words: 0, lines: 0))
        XCTAssertEqual(TextTools.statistics("👩🏽‍💻"), TextStatistics(characters: 1, words: 1, lines: 1))
        let lineStats = TextTools.statistics("a\r\nb\r")
        XCTAssertEqual(lineStats.words, 2)
        XCTAssertEqual(lineStats.lines, 3)
    }

    func testRouteAllowsNavigationAndRejectsUnexpectedPayloads() throws {
        let id = UUID()
        let route = try XCTUnwrap(URL(string: "myapp://record/\(id.uuidString)"))
        XCTAssertEqual(StarterRoute.parse(route, scheme: "myapp"), .record(id))
        for string in ["other://collection", "myapp://delete/123", "myapp://record/not-a-uuid",
                       "myapp://collection?delete=all", "myapp://utility/extra",
                       "myapp://user:pass@settings", "myapp://utility#extra"] {
            let url = try XCTUnwrap(URL(string: string))
            XCTAssertNil(StarterRoute.parse(url, scheme: "myapp"), string)
        }
    }

    func testStoreRoundTripKeepsIdentityAndMissingIsDistinctFromCorruption() throws {
        let directory = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString)
        defer { try? FileManager.default.removeItem(at: directory) }
        let store = LocalFileStore(directory: directory)
        XCTAssertNil(try store.load([LifestyleRecord].self, filename: "records.json"))
        let date = Date(timeIntervalSince1970: 1_700_000_000.125)
        let records = [LifestyleRecord(title: "Cây A", notes: "Ghi chú", updatedAt: date),
                       LifestyleRecord(title: "Cây A", updatedAt: date)]
        try store.save(records, filename: "records.json")
        XCTAssertEqual(try store.load([LifestyleRecord].self, filename: "records.json"), records)
        try Data("invalid json".utf8).write(to: directory.appendingPathComponent("records.json"))
        XCTAssertThrowsError(try store.load([LifestyleRecord].self, filename: "records.json"))
        XCTAssertThrowsError(try store.save(records, filename: "../escape.json"))
    }

    func testFailedReplacementDoesNotEraseExistingFile() throws {
        struct CannotEncode: Encodable {
            func encode(to encoder: Encoder) throws {
                throw EncodingError.invalidValue("fixture", .init(codingPath: [], debugDescription: "Intentional test failure"))
            }
        }
        let directory = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString)
        defer { try? FileManager.default.removeItem(at: directory) }
        let store = LocalFileStore(directory: directory)
        try store.save(["preserve"], filename: "existing.json")
        XCTAssertThrowsError(try store.save(CannotEncode(), filename: "existing.json"))
        XCTAssertEqual(try store.load([String].self, filename: "existing.json"), ["preserve"])
    }
}
