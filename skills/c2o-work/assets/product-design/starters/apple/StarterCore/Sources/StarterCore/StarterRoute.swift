import Foundation

public enum StarterRoute: Equatable, Sendable {
    case collection
    case record(UUID)
    case utility
    case settings

    /// Routing only. A URL never triggers create, edit, delete or processing.
    public static func parse(_ url: URL, scheme: String = AppProfile.urlScheme) -> StarterRoute? {
        guard url.scheme?.lowercased() == scheme.lowercased(),
              url.user == nil, url.password == nil, url.port == nil,
              url.query == nil, url.fragment == nil,
              let host = url.host?.lowercased() else { return nil }
        let parts = url.pathComponents.filter { $0 != "/" }
        switch (host, parts.count) {
        case ("collection", 0): return .collection
        case ("utility", 0): return .utility
        case ("settings", 0): return .settings
        case ("record", 1):
            guard let id = UUID(uuidString: parts[0]) else { return nil }
            return .record(id)
        default: return nil
        }
    }
}
