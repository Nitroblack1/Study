#include <iostream>

using namespace std;

constexpr int MAX_NODE_NUM = 10000;
constexpr int MAX_CHILD_NUM = 2;

struct TreeNode {
    int parent;
    int child[MAX_CHILD_NUM];
};

TreeNode tree[MAX_NODE_NUM + 1];
int nodeNum, edgeNum, rootNode;

void initTree() {
    for (int i = 0; i <= nodeNum; ++i) {
        tree[i].parent = -1;
        for (int j = 0; j < MAX_CHILD_NUM; ++j) {
            tree[i].child[j] = -1;
        }
    }
}

void addChild(int parent, int child) {
    int i = 0;
    for (; i < MAX_CHILD_NUM; i++) {
        if (tree[parent].child[i] == -1) break;
    }

    tree[parent].child[i] = child;
    tree[child].parent = parent;
};

int getRoot() {
    for (int i = 1; i <= nodeNum; i++) {
        if (tree[i].parent == -1) {
            return i;
        }
    }
    return -1;
}

void preOrder(int r) {
    cout << r << ' ';
    for (int i = 0; i < MAX_CHILD_NUM; i++) {
        int c = tree[r].child[i];
        if (c != -1) {
            preOrder(c);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> nodeNum >> edgeNum;

        initTree();

        for (int i = 0; i < edgeNum; i++) {
            int parent, child;
            cin >> parent >> child;
            addChild(parent, child);
        }

        rootNode = getRoot();

        cout << "#" << test_case << ' ';
        preOrder(rootNode);
        cout << '\n';
    }

    return 0;
}