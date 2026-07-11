#include <vector>
#include <unordered_set>

class Solution {
public:
    int countCompleteComponents(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        std::vector<bool> visited(n, false);
        int completeComponentsCount = 0;

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                int nodeCount = 0;
                int edgeCount = 0;

                auto dfs = [&](auto& self, int u) -> void {
                    visited[u] = true;
                    nodeCount++;
                    edgeCount += adj[u].size(); 
                    for (int neighbor : adj[u]) {
                        if (!visited[neighbor]) {
                            self(self, neighbor);
                        }
                    }
                };

                dfs(dfs, i);

                if (edgeCount == nodeCount * (nodeCount - 1)) {
                    completeComponentsCount++;
                }
            }
        }

        return completeComponentsCount;
    }
};
