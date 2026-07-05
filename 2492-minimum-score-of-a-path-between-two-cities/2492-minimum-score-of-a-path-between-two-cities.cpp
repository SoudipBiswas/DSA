class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int, int>>> graph(n + 1);
        for (const auto& road : roads) {
            int u = road[0], v = road[1], w = road[2];
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        queue<int> q;
        q.push(1);
        vector<bool> visited(n + 1, false);
        visited[1] = true;
        
        int min_score = INT_MAX;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (const auto& neighbor : graph[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;
                
                min_score = min(min_score, weight);

                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }

        return min_score;
    }
};
