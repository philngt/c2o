import Foundation

public enum StarterCategory: String, Codable, Sendable {
    case lifestyle
    case utility
}

/// The generator supplies the same keys to the app and its widget extension.
public enum AppProfile {
    public static var category: StarterCategory {
        StarterCategory(rawValue: value("C2OCategory", fallback: "utility")) ?? .utility
    }
    public static var displayName: String {
        value("C2OAppDisplayName", fallback: "C2O Starter")
    }
    public static var urlScheme: String {
        value("C2OURLScheme", fallback: "c2ostarter")
    }
    public static var appGroupID: String {
        value("C2OAppGroupID", fallback: "")
    }
    public static var widgetsEnabled: Bool {
        Bundle.main.object(forInfoDictionaryKey: "C2OWidgetsEnabled") as? Bool ?? false
    }
    public static let widgetKind = "C2OSummaryWidget"

    private static func value(_ key: String, fallback: String) -> String {
        guard let result = Bundle.main.object(forInfoDictionaryKey: key) as? String,
              !result.isEmpty else { return fallback }
        return result
    }
}

public struct LifestyleRecord: Identifiable, Codable, Equatable, Sendable {
    public var id: UUID
    public var title: String
    public var notes: String
    public var isFavorite: Bool
    public var updatedAt: Date

    public init(id: UUID = UUID(), title: String, notes: String = "",
                isFavorite: Bool = false, updatedAt: Date = Date()) {
        self.id = id
        self.title = title
        self.notes = notes
        self.isFavorite = isFavorite
        self.updatedAt = updatedAt
    }
}

public struct UtilityHistoryItem: Identifiable, Codable, Equatable, Sendable {
    public var id: UUID
    public var input: String
    public var output: String
    public var createdAt: Date

    public init(id: UUID = UUID(), input: String, output: String,
                createdAt: Date = Date()) {
        self.id = id
        self.input = input
        self.output = output
        self.createdAt = createdAt
    }
}

public struct TextStatistics: Equatable, Sendable {
    public let characters: Int
    public let words: Int
    public let lines: Int

    public init(characters: Int, words: Int, lines: Int) {
        self.characters = characters
        self.words = words
        self.lines = lines
    }
}

/// A compact snapshot; the starter publishes counts/status, never notes/input text.
public struct WidgetSnapshot: Codable, Equatable, Sendable {
    public var category: String
    public var title: String
    public var subtitle: String
    public var updatedAt: Date
    public var route: String

    public init(category: String, title: String, subtitle: String,
                updatedAt: Date, route: String) {
        self.category = category
        self.title = title
        self.subtitle = subtitle
        self.updatedAt = updatedAt
        self.route = route
    }
}
