#include "parser.hpp"
#include <sstream>
#include <iostream>

std::vector<CodeMetricNode> SovereignParser::analyze_codebase(std::string_view source) {
    std::vector<CodeMetricNode> metrics;
    std::string content(source);
    std::istringstream stream(content);
    std::string line;
    int current_line = 0;

    while (std::getline(stream, line)) {
        current_line++;

        // 1. فحص حقيقي لتسريب الأسرار والـ Hardcoded Tokens
        if (line.find("secret") != std::string::npos || line.find("api_key") != std::string::npos) {
            if (line.find("=") != std::string::npos) {
                metrics.push_back({
                    .entity_name = "Hardcoded_Credential_Line_" + std::to_string(current_line),
                    .type = "Variable_Assignment",
                    .line_start = current_line,
                    .is_vulnerable = true,
                    .risk_category = "Hardcoded_Secret"
                });
            }
        }

        // 2. فحص حقيقي لاستخدام خوارزميات تشفير مكسورة أو ضعيفة
        if (line.find("MD5") != std::string::npos || line.find("md5") != std::string::npos || line.find("SHA1") != std::string::npos) {
            metrics.push_back({
                .entity_name = "Weak_Crypto_Usage_At_" + std::to_string(current_line),
                .type = "Crypto_Call",
                .line_start = current_line,
                .is_vulnerable = true,
                .risk_category = "Insecure_Crypto"
            });
        }

        // 3. فحص بنية الدوال والمعمارية البرمجية
        if ((line.find("void ") != std::string::npos || line.find("def ") != std::string::npos) && line.find("(") != std::string::npos) {
            metrics.push_back({
                .entity_name = "Function_Definition_At_" + std::to_string(current_line),
                .type = "Architecture_Component",
                .line_start = current_line,
                .is_vulnerable = false,
                .risk_category = "Clean"
            });
        }
    }
    return metrics;
}

nlohmann::json SovereignParser::serialize_to_json(const std::vector<CodeMetricNode>& metrics, std::string_view file_name) {
    nlohmann::json root = nlohmann::json::object();
    root["file_name"] = file_name;
    root["analyzer_signature"] = "Alaa_Sovereign_Engine_v1.0";
    root["findings"] = nlohmann::json::array();

    for (const auto& item : metrics) {
        nlohmann::json node = {
            {"entity", item.entity_name},
            {"type", item.type},
            {"line", item.line_start},
            {"vulnerable", item.is_vulnerable},
            {"category", item.risk_category}
        };
        root["findings"].push_back(node);
    }
    return root;
}
