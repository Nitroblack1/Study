#include <iostream>

using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;

    Node(int item) : key(item), left(nullptr), right(nullptr) {}
};

Node* current = nullptr;

Node* addRec(Node* node, int key) {
    if (node == nullptr) return new Node(key);  // Create a new node if we reach a null position

    if (key < node->key) node->left = addRec(node->left, key);
    else if (key > node->key) node->right = addRec(node->right, key);

    return node;
}

void add(int key) {
    current = addRec(current, key);     // Insert the key into the tree
}

bool findRec(Node* node, int key) {
    if (node != nullptr) {
        if (key == node->key) return true;
        if (findRec(node->left, key)) return true;
        if (findRec(node->right, key)) return true;
    }
    return false;
}

bool contains(int key) {
    return findRec(current, key);       // Check if the key exists in the tree
}

void printAll(Node* node) {
    if (node != nullptr) {
        printAll(node->left);           // Traverse left subtree
        cout << node->key << " ";       // Print the current node's key
        printAll(node->right);          // Traverse right subtree
    }
}

void printAll() {
    printAll(current);                  // Print all keys in the tree
}

Node* minValueNode(Node* node) {
    Node* cur = node;
    while (cur->left != nullptr) cur = cur->left; // Find the leftmost node
    return cur;
}

Node* removeRec(Node* node, int key) {
    if (node == nullptr) return node;

    if (key < node->key) {
        node->left = removeRec(node->left, key);
    } else if (key > node->key) {
        node->right = removeRec(node->right, key);
    } else {
        if (node->left == nullptr) {
            Node* temp = node->right;
            delete node;
            return temp;
        } else if (node->right == nullptr) {
            Node* temp = node->left;
            delete node;
            return temp;
        }

        Node* temp = minValueNode(node->right);
        node->key = temp->key;
        node->right = removeRec(node->right, temp->key);
    }

    return node;
}

void removeKey(int key) {
    current = removeRec(current, key); // Remove the key from the tree
}

void destroyTree(Node* node) {
    if (!node) return;
    destroyTree(node->left);
    destroyTree(node->right);
    delete node;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, N;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        destroyTree(current);
        current = nullptr;

        cin >> N;
        for (int i = 0; i < N; ++i) {
            int cmd, key;
            cin >> cmd >> key;

            switch (cmd) {
                case 1: add(key); break;
                case 2: removeKey(key); break;
            }
        }

        cout << "#" << test_case << ' ';
        printAll();
        cout << "\n";
    }

    destroyTree(current);
    current = nullptr;

    return 0;
}