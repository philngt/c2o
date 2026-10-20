import Foundation

public enum StarterStorageError: LocalizedError {
    case invalidFilename
    case appGroupUnavailable

    public var errorDescription: String? {
        switch self {
        case .invalidFilename: return "Tên tệp lưu trữ không hợp lệ."
        case .appGroupUnavailable: return "Chưa thể truy cập dữ liệu dùng chung của widget."
        }
    }
}

/// Small local starter data, one app writer. This is not a database or sync engine.
/// Methods are synchronous; move to a serialized repository for large datasets.
public struct LocalFileStore {
    private let suppliedDirectory: URL?

    public init(directory: URL? = nil) { suppliedDirectory = directory }

    public func load<T: Decodable>(_ type: T.Type, filename: String) throws -> T? {
        let url = try fileURL(filename: filename, createDirectory: false)
        let data: Data
        do {
            data = try Data(contentsOf: url)
        } catch let error as NSError {
            // A corrupt or unreadable file must never become a fake empty collection.
            if error.domain == NSCocoaErrorDomain && error.code == NSFileReadNoSuchFileError {
                return nil
            }
            throw error
        }
        return try Self.decoder().decode(T.self, from: data)
    }

    public func save<T: Encodable>(_ value: T, filename: String) throws {
        let url = try fileURL(filename: filename, createDirectory: true)
        let data = try Self.encoder().encode(value)
        try data.write(to: url, options: .atomic)
    }

    private func fileURL(filename: String, createDirectory: Bool) throws -> URL {
        guard !filename.isEmpty, filename != ".", filename != "..",
              !filename.contains("/"), !filename.contains("\\"),
              !filename.contains("\0") else { throw StarterStorageError.invalidFilename }
        let directory: URL
        if let suppliedDirectory {
            directory = suppliedDirectory
        } else {
            let support = try FileManager.default.url(for: .applicationSupportDirectory,
                in: .userDomainMask, appropriateFor: nil, create: createDirectory)
            directory = support.appendingPathComponent(
                Bundle.main.bundleIdentifier ?? "C2OStarter", isDirectory: true)
        }
        if createDirectory {
            try FileManager.default.createDirectory(at: directory,
                withIntermediateDirectories: true)
        }
        return directory.appendingPathComponent(filename, isDirectory: false)
    }

    private static func encoder() -> JSONEncoder {
        let encoder = JSONEncoder()
        // Preserve Date's fractional seconds; app and widget use the same codec.
        encoder.dateEncodingStrategy = .deferredToDate
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
        return encoder
    }

    private static func decoder() -> JSONDecoder {
        let decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .deferredToDate
        return decoder
    }
}

/// Only the app writes this snapshot. The widget reads it and never edits app records.
public enum WidgetSnapshotStore {
    private static let filename = "widget-summary-v1.json"

    public static func write(_ snapshot: WidgetSnapshot) throws {
        let store = try sharedStore()
        try store.save(snapshot, filename: filename)
    }

    public static func read() throws -> WidgetSnapshot? {
        try sharedStore().load(WidgetSnapshot.self, filename: filename)
    }

    private static func sharedStore() throws -> LocalFileStore {
        guard AppProfile.widgetsEnabled, !AppProfile.appGroupID.isEmpty else {
            throw StarterStorageError.appGroupUnavailable
        }
        #if os(iOS) || os(macOS)
        guard let container = FileManager.default.containerURL(
            forSecurityApplicationGroupIdentifier: AppProfile.appGroupID) else {
            throw StarterStorageError.appGroupUnavailable
        }
        return LocalFileStore(directory: container.appendingPathComponent("C2OSnapshots", isDirectory: true))
        #else
        throw StarterStorageError.appGroupUnavailable
        #endif
    }
}
