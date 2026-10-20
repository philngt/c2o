// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "StarterCore",
    platforms: [.iOS(.v17), .macOS(.v14)],
    products: [.library(name: "StarterCore", targets: ["StarterCore"])],
    targets: [
        .target(name: "StarterCore"),
        .testTarget(name: "StarterCoreTests", dependencies: ["StarterCore"])
    ]
)
