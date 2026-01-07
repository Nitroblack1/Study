#include <iostream>

using namespace std;

struct AdjListNode {
    int vertex;
    AdjListNode *next;

    AdjListNode(int v) : vertex(v), next(nullptr) {}    // {}는 생성자의 몸체를 의미한다. 즉, 생성자 실행 블록이다.
};

struct AdjList {
    int num_members;
    AdjListNode* head;
    AdjListNode* tail;

    AdjList() : num_members(0), head(nullptr), tail(nullptr) {}
};

struct Graph {
    int num_vertices;
    AdjList* adjListArr;

    Graph(int n) : num_vertices(n) {    // num vertices 초기화
        adjListArr = new AdjList[n];    // n개의 AdjList로 이루어진 배열 동적 할당
    }

    ~Graph() {
        // 모든 인접 리스트 노드 해제
        for (int v = 0; v < num_vertices; v++) {
            AdjListNode* cur = adjListArr[v].head;
            while (cur) {
                AdjListNode* temp = cur;
                cur = cur->next;
                delete temp;
            }
        }

        delete[] adjListArr;    // 인접 리스트 배열 해제
    }
};

void addEdge(Graph* graph, int src, int dest) {
    // src -> dest 간선 추가
    AdjListNode* newNode = new AdjListNode(dest);

    if (graph->adjListArr[src].tail != nullptr) {   // 비어있지 않은 경우
        graph->adjListArr[src].tail->next = newNode;    // 마지막 노드의 next를 새 노드로 연결
        graph->adjListArr[src].tail = newNode;  // tail 갱신
    } else {    // 비어있는 경우
        graph->adjListArr[src].head = graph->adjListArr[src].tail = newNode;    // head와 tail을 새 노드로 초기화
    }
    graph->adjListArr[src].num_members++;
}

void displayGraph(Graph* graph, int i) {
    AdjListNode* cur = graph->adjListArr[i].head;
    while (cur) {
        cout << cur->vertex << ' ';
        cur = cur->next;
    }
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, V, E, Q, sv, ev;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> V >> E >> Q;

        Graph* graph = new Graph(V);

        for (int i = 0; i < E; i++) {
            cin >> sv >> ev;
            addEdge(graph, sv, ev);
        }

        cout << "#" << test_case << '\n';

        for (int i = 0; i < Q; i++) {
            int query_vertex;
            cin >> query_vertex;
            displayGraph(graph, query_vertex);
        }

        delete graph;
    }

    return 0;
}