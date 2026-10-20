import Foundation

public enum TextTools {
    /// Collapses all whitespace (including line breaks) to one space.
    /// This is a declared transform, not a language-aware rewrite.
    public static func normalizedWhitespace(_ text: String) -> String {
        text.split(whereSeparator: { $0.isWhitespace }).joined(separator: " ")
    }

    /// Characters are Swift grapheme clusters; words are whitespace-separated tokens.
    /// Empty text has zero lines; CRLF and CR are normalized to LF for line counting.
    public static func statistics(_ text: String) -> TextStatistics {
        let normalizedLines = text.replacingOccurrences(of: "\r\n", with: "\n")
            .replacingOccurrences(of: "\r", with: "\n")
        return TextStatistics(
            characters: text.count,
            words: text.split(whereSeparator: { $0.isWhitespace }).count,
            lines: text.isEmpty ? 0 : normalizedLines.components(separatedBy: "\n").count
        )
    }
}
