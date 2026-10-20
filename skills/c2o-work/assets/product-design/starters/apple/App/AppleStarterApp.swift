import SwiftUI
import StarterCore

@main
@MainActor
struct AppleStarterApp: App {
    @StateObject private var model = StarterAppModel()

    var body: some Scene {
        #if os(macOS)
        // One main window and one app-owned writer; this is not a document app.
        Window(AppProfile.displayName, id: "main") {
            StarterRootView().environmentObject(model)
        }
        .commands { StarterCommands(model: model) }

        Settings {
            StarterSettingsView()
                .environmentObject(model)
                .frame(minWidth: 360, idealWidth: 440, minHeight: 320)
        }
        #else
        // The generated iOS Info.plist disables multiple scenes.
        WindowGroup {
            StarterRootView().environmentObject(model)
        }
        #endif
    }
}

@MainActor
private struct StarterRootView: View {
    @EnvironmentObject private var model: StarterAppModel
    #if os(macOS)
    @Environment(\.openSettings) private var openSettings
    #endif

    var body: some View {
        Group {
            switch AppProfile.category {
            case .lifestyle: LifestyleCollectionRoot()
            case .utility: UtilityWorkbenchRoot()
            }
        }
        .sheet(item: $model.sheet, onDismiss: openPendingRoute) { sheet in
            switch sheet {
            case .editor(let request):
                RecordEditorView(record: request.record)
                    .environmentObject(model)
            case .settings:
                NavigationStack {
                    StarterSettingsView()
                        .toolbar {
                            ToolbarItem(placement: .confirmationAction) {
                                Button("Xong") { model.sheet = nil }
                            }
                        }
                }
                .environmentObject(model)
            case .history:
                UtilityHistorySheet().environmentObject(model)
            }
        }
        .alert("Chưa hoàn tất thao tác", isPresented: Binding(
            get: { model.actionError != nil },
            set: { if !$0 { model.actionError = nil } }
        )) {
            Button("Đóng", role: .cancel) { model.actionError = nil }
        } message: {
            Text(model.actionError ?? "")
        }
        .safeAreaInset(edge: .bottom) {
            if let warning = model.widgetWarning {
                NoticeBanner(message: warning) {
                    Button("Thử lại") { model.publishWidgetSnapshot() }
                    Button("Đóng") { model.widgetWarning = nil }
                }
            }
        }
        .onOpenURL { url in
            guard let route = StarterRoute.parse(url) else { return }
            if let presentedSheet = model.sheet {
                // Finish or cancel an editor before acting on another presentation.
                model.pendingRoute = route
                switch presentedSheet {
                case .editor:
                    return
                case .settings, .history:
                    model.sheet = nil
                }
            } else {
                open(route)
            }
        }
    }

    private func openPendingRoute() {
        guard let route = model.pendingRoute else { return }
        model.pendingRoute = nil
        open(route)
    }

    private func open(_ route: StarterRoute) {
        if route == .settings {
            #if os(macOS)
            openSettings()
            #else
            model.sheet = .settings
            #endif
        } else {
            model.navigate(to: route)
        }
    }
}

#if os(macOS)
@MainActor
private struct StarterCommands: Commands {
    @ObservedObject var model: StarterAppModel
    @Environment(\.openWindow) private var openWindow

    var body: some Commands {
        CommandGroup(replacing: .newItem) {
            Button(AppProfile.category == .lifestyle ? "Mục mới" : "Văn bản mới") {
                openWindow(id: "main")
                model.requestNewItem()
            }
            .keyboardShortcut("n", modifiers: .command)
            .disabled(model.sheet != nil ||
                (AppProfile.category == .lifestyle && !model.collectionReady))
        }
        // SwiftUI supplies the standard Settings command for the Settings scene.
    }
}
#endif
