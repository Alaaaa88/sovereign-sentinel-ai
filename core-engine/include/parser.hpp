#pragma once
#include <string>
#include <vector>
#include <concepts>
#include <string_view>
#include <nlohmann/json.hpp>

struct CodeMetricNode {
    std::string entity_name;   // اسم الدالة أو الكلاس
    std::string type;          // Function, Class, Control_Flow
    int line_start;
    bool is_vulnerable;
    std::string risk_category; // Insecure_Crypto, Hardcoded_Secret, Clean
};

template<typename T>
concept AdvancedCodeAnalyzer = requires(T analyzer, std::string_view source) {
    { analyzer.analyze_codebase(source) } -> std::same_as<std::vector<CodeMetricNode>>;
};

class SovereignParser {
public:
    std::vector<CodeMetricNode> analyze_codebase(std::string_view source);
    nlohmann::json serialize_to_json(const std::vector<CodeMetricNode>& metrics, std::string_view file_name);
};
