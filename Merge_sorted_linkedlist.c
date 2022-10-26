struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode  head;
    struct ListNode   *h=&head;
    if(l1==NULL && l2==NULL)
        return NULL;
    
    while(l1 && l2){
        if(l1->val < l2->val){
          h->next=l1;
            l1=l1->next;
            h=h->next;
        }
        else
        {
            h->next=l2;
            l2=l2->next;
            h=h->next;
        }
    }
    if(l1){
        h->next=l1;
        }
    if(l2){
        h->next=l2;
    }
    return head.next;
}
