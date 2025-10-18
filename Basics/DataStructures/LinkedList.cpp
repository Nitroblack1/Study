#include <iostream>
using namespace std;

struct ListNode
{
    int data;
    struct ListNode* prev;
    struct ListNode* next;
};

ListNode* list_create(int _data)
{
    ListNode* node = new ListNode;
    node->prev = nullptr;
    node->next = nullptr;
    node->data = _data;
    return node;
}

ListNode* list_insert(ListNode* _head, ListNode* new_node)
{
    ListNode* next = _head->next;

    _head->next = new_node;
    new_node->next = next;
    new_node->prev = _head;

    if (next != nullptr) {
        next->prev = new_node;
    }

    return new_node;
}

int list_erase(ListNode* head, int _data) {
    ListNode* it = head->next;
    int ret = 0;

    while (it != nullptr) {
        if (it->data == _data) {
            ListNode* prev = it->prev;
            ListNode* next = it->next;
            ListNode* tmp = it;
            it = it->next;

            prev->next = next;
            if (next != nullptr) {
                next->prev = prev;
            }

            delete tmp;
            ret++;
        } else {
            it = it->next;
        }
    }

    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, N;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> N;

        ListNode* head = list_create(0); // sentinel node (0 as dummy)
        cout << "#" << test_case;

        for (int i = 0; i < N; i++) {
            int mode, data;
            cin >> mode >> data;

            if (mode == 1) {
                ListNode* node = list_create(data);
                list_insert(head, node);
            } else if (mode == 2) {
                cout << " " << list_erase(head, data);
            }
        }

        // Free all nodes
        while (head != nullptr) {
            ListNode* tmp = head;
            head = head->next;
            delete tmp;
        }

        cout << "\n";
    }

    return 0;
}