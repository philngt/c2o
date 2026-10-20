import Foundation
import StarterCore
import SwiftUI
import WidgetKit

// Add this source to the iOS or macOS widget extension, not the host app target.
// Baseline: iOS/iPadOS 17 and macOS 14. The extension only reads a published summary.
@main
struct C2OSummaryWidgets: WidgetBundle {
    var body: some Widget {
        C2OSummaryWidget()
    }
}

struct C2OSummaryWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: AppProfile.widgetKind,
            provider: SummaryTimelineProvider()
        ) { entry in
            SummaryWidgetView(entry: entry)
                .containerBackground(for: .widget) {
                    Rectangle().fill(.background)
                }
                .widgetURL(entry.destinationURL)
        }
        .configurationDisplayName("Bản tóm tắt")
        .description("Xem thông tin đã lưu và mở ứng dụng để tiếp tục.")
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}

private enum SummaryState {
    case available(WidgetSnapshot)
    case missing
    case unavailable
    case preview
    case placeholder
}

private struct SummaryEntry: TimelineEntry {
    let date: Date
    let state: SummaryState

    static var defaultRoute: String {
        AppProfile.category == .lifestyle ? "collection" : "utility"
    }

    var snapshot: WidgetSnapshot? {
        if case .available(let value) = state { return value }
        return nil
    }

    var isIllustration: Bool {
        switch state {
        case .preview, .placeholder: return true
        default: return false
        }
    }

    var title: String {
        switch state {
        case .available(let value): return value.title
        case .missing: return "Chưa có bản tóm tắt"
        case .unavailable: return "Chưa đọc được bản tóm tắt"
        case .preview, .placeholder: return "Bản tóm tắt của bạn"
        }
    }

    var subtitle: String {
        switch state {
        case .available(let value): return value.subtitle
        case .missing: return "Mở ứng dụng để bắt đầu."
        case .unavailable: return "Mở ứng dụng để kiểm tra và thử lại."
        case .preview, .placeholder: return "Nội dung minh họa, chưa phải dữ liệu của bạn."
        }
    }

    var symbol: String {
        switch state {
        case .unavailable: return "exclamationmark.circle"
        case .missing: return "square.dashed"
        default:
            return AppProfile.category == .lifestyle ? "leaf" : "wrench.and.screwdriver"
        }
    }

    var destinationURL: URL? {
        // Only an allowlisted, read-only destination. Never encode a mutation or user input.
        let candidate = snapshot?.route ?? Self.defaultRoute
        let route = ["collection", "utility"].contains(candidate) ? candidate : Self.defaultRoute
        var components = URLComponents()
        components.scheme = AppProfile.urlScheme
        components.host = route
        return components.url
    }
}

private struct SummaryTimelineProvider: TimelineProvider {
    func placeholder(in context: Context) -> SummaryEntry {
        // No disk or network work. The system may redact this temporary stand-in.
        SummaryEntry(date: Date(), state: .placeholder)
    }

    func getSnapshot(in context: Context, completion: @escaping (SummaryEntry) -> Void) {
        if context.isPreview {
            completion(SummaryEntry(date: Date(), state: .preview))
        } else {
            completion(readEntry())
        }
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<SummaryEntry>) -> Void) {
        let entry = readEntry()
        // Content changes only when the host app publishes a new summary.
        // After a successful publish the host requests reloadTimelines(ofKind:).
        // .never avoids a polling promise; WidgetKit still decides when to reload.
        completion(Timeline(entries: [entry], policy: .never))
    }

    private func readEntry() -> SummaryEntry {
        let now = Date()
        guard AppProfile.widgetsEnabled else {
            return SummaryEntry(date: now, state: .unavailable)
        }
        do {
            guard let snapshot = try WidgetSnapshotStore.read() else {
                return SummaryEntry(date: now, state: .missing)
            }
            // A stale file from another category or an unsupported route is not valid content.
            guard snapshot.category == AppProfile.category.rawValue,
                  snapshot.route == SummaryEntry.defaultRoute,
                  !snapshot.title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else {
                return SummaryEntry(date: now, state: .unavailable)
            }
            return SummaryEntry(date: now, state: .available(snapshot))
        } catch {
            // A read/decoding/group-configuration error is not an empty collection.
            // Never replace this with a demo record or expose raw diagnostic text in the widget.
            return SummaryEntry(date: now, state: .unavailable)
        }
    }
}

private struct SummaryWidgetView: View {
    @Environment(\.widgetFamily) private var family
    let entry: SummaryEntry

    var body: some View {
        Group {
            switch family {
            case .systemMedium:
                mediumContent
            case .systemLarge:
                largeContent
            default:
                smallContent
            }
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
        .accessibilityElement(children: .combine)
        .accessibilityHint("Mở ứng dụng để xem thêm.")
    }

    private var heading: some View {
        HStack(alignment: .firstTextBaseline, spacing: 5) {
            Image(systemName: entry.symbol)
                .accessibilityHidden(true)
            Text(AppProfile.displayName)
                .lineLimit(1)
            if entry.isIllustration {
                Spacer(minLength: 0)
                Text("Minh họa")
                    .fontWeight(.semibold)
                    .lineLimit(1)
            }
        }
        .font(.caption2)
        .foregroundStyle(.secondary)
    }

    private var smallContent: some View {
        VStack(alignment: .leading, spacing: 6) {
            heading
            Text(entry.title)
                .font(.headline)
                .lineLimit(3)
            Text(entry.subtitle)
                .font(.caption2)
                .foregroundStyle(.secondary)
                .lineLimit(2)
            Spacer(minLength: 0)
            if let snapshot = entry.snapshot {
                Text(snapshot.updatedAt, format: .dateTime.day().month().year())
                    .font(.caption2)
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
                    .accessibilityLabel("Cập nhật \(snapshot.updatedAt.formatted(date: .abbreviated, time: .shortened))")
            }
        }
    }

    private var mediumContent: some View {
        HStack(alignment: .top, spacing: 16) {
            VStack(alignment: .leading, spacing: 10) {
                heading
                Text(entry.title)
                    .font(.headline)
                    .lineLimit(3)
                Spacer(minLength: 0)
            }
            .frame(maxWidth: .infinity, alignment: .leading)

            VStack(alignment: .leading, spacing: 8) {
                Text(entry.subtitle)
                    .font(.subheadline)
                    .lineLimit(4)
                Spacer(minLength: 0)
                freshness
            }
            .frame(maxWidth: .infinity, alignment: .leading)
        }
    }

    private var largeContent: some View {
        VStack(alignment: .leading, spacing: 14) {
            heading
            Text(entry.title)
                .font(.title2.weight(.semibold))
                .lineLimit(4)
            Text(entry.subtitle)
                .font(.body)
                .foregroundStyle(.secondary)
                .lineLimit(5)
            Spacer(minLength: 0)
            freshness
            Divider()
            Label("Xem trong ứng dụng", systemImage: "arrow.up.forward")
                .font(.subheadline)
        }
    }

    @ViewBuilder
    private var freshness: some View {
        if let snapshot = entry.snapshot {
            VStack(alignment: .leading, spacing: 2) {
                Text("Cập nhật")
                Text(snapshot.updatedAt, format: .dateTime.day().month().year().hour().minute())
            }
            .font(.caption2)
            .foregroundStyle(.secondary)
        } else if entry.isIllustration {
            Text("Ví dụ xem trước")
                .font(.caption2)
                .foregroundStyle(.secondary)
        } else {
            Text("Tiếp tục trong ứng dụng")
                .font(.caption2)
                .foregroundStyle(.secondary)
        }
    }
}
