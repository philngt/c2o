import SwiftUI
#if os(iOS)
import UIKit
#endif

@MainActor
enum StarterDevice {
    static var usesPhoneNavigation: Bool {
        #if os(iOS)
        return UIDevice.current.userInterfaceIdiom == .phone
        #else
        return false
        #endif
    }
}

@MainActor
struct StarterSettingsControl: View {
    @EnvironmentObject private var model: StarterAppModel

    var body: some View {
        #if os(macOS)
        SettingsLink { Label("Cài đặt", systemImage: "gearshape") }
            .labelStyle(.iconOnly)
        #else
        Button {
            guard model.sheet == nil else { return }
            model.sheet = .settings
        } label: {
            Label("Cài đặt", systemImage: "gearshape")
        }
        .labelStyle(.iconOnly)
        #endif
    }
}

@MainActor
struct LoadFailureView: View {
    let title: String
    let detail: String
    let retry: () -> Void

    var body: some View {
        ContentUnavailableView {
            Label(title, systemImage: "exclamationmark.triangle")
        } description: {
            Text("Dữ liệu cũ chưa bị thay thế. \(detail)")
        } actions: {
            Button("Thử đọc lại", action: retry)
                .buttonStyle(.bordered)
        }
    }
}

@MainActor
struct NoticeBanner<Actions: View>: View {
    let message: String
    let actions: () -> Actions

    init(message: String, @ViewBuilder actions: @escaping () -> Actions) {
        self.message = message
        self.actions = actions
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Label(message, systemImage: "exclamationmark.triangle")
                .font(.callout)
                .fixedSize(horizontal: false, vertical: true)
            HStack { actions() }
                .buttonStyle(.bordered)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(.regularMaterial)
    }
}
