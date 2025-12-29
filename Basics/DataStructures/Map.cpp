#include <iostream>
using namespace std;

struct Node {
    int key;
    int value;
    Node* left;
    Node* right;

    Node(int k, int v) : key(k), value(v), left(nullptr), right(nullptr) {}
};

Node* current = nullptr;

Node* putRec(Node* node, int key, int value) {
    if (node == nullptr) return new Node(key, value);

    if (key < node->key) node->left = putRec(node->left, key, value);
    else if (key > node->key) node->right = putRec(node->right, key, value);
    else node->value = value;

    return node;
}

void put(int key, int value) {
    current = putRec(current, key, value);
}

int findRec(Node* node, int key) {
    if (node != nullptr) {
        if (key == node->key) return node->value;

        int ret = findRec(node->left, key);
        if (ret != -1) return ret;

        ret = findRec(node->right, key);
        if (ret != -1) return ret;
    }
    return -1;
}

bool contains(int key) {
    return findRec(current, key) != -1;
}

int get(int key) {
    return findRec(current, key);
}

Node* minValueNode(Node* node) {
    Node* cur = node;
    while (cur && cur->left != nullptr) cur = cur->left;
    return cur;
}

Node* removeRec(Node* node, int key) {
    if (node == nullptr) return nullptr;

    if (key < node->key) {
        node->left = removeRec(node->left, key);
    } else if (key > node->key) {
        node->right = removeRec(node->right, key);
    } else {
        // 삭제할 노드 발견
        if (node->left == nullptr) {
            Node* temp = node->right;
            delete node;
            return temp;
        } else if (node->right == nullptr) {
            Node* temp = node->left;
            delete node;
            return temp;
        }

        // 자식 2개: 오른쪽 서브트리의 최소 노드를 가져옴
        Node* temp = minValueNode(node->right);
        node->key = temp->key;
        node->value = temp->value;
        node->right = removeRec(node->right, temp->key);
    }

    return node;
}

void removeKey(int key) {
    current = removeRec(current, key);
}

void deleteTree(Node* node) {
    if (!node) return;
    deleteTree(node->left);
    deleteTree(node->right);
    delete node;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, N;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        deleteTree(current);
        current = nullptr;

        cin >> N;
        cout << "#" << test_case << " ";

        for (int i = 0; i < N; ++i) {
            int cmd, key;
            cin >> cmd >> key;

            if (cmd == 1) {
                int value;
                cin >> value;
                put(key, value);
            } else if (cmd == 2) {
                removeKey(key);
            } else if (cmd == 3) {
                int ret = get(key);
                cout << ret << " ";
            }
        }
        cout << "\n";
    }

    deleteTree(current);
    current = nullptr;

    return 0;
}