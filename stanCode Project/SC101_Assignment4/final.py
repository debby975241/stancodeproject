

# Problem 1 is LC1845(but using no for loop)
def __init__ (self, n):
    self.available = [True]*n
    self.n = n

def reserve(self):
    for i in range(len(self.available)):
        if self.available[i]:
            self.available[i] = False
            return i+1

def unreserve(self):
    self.available[self.n-1] = True


# Problem 2
def get_dict():
    all_d = {}
    male_d = {}
    female_d = {}
    with open (FILE, 'r') as f:
        for line in f:
            line = line.strip()
            lst = line.split(',')
            lst.pop(0)
            highest = len(lst)//2
            for i in range(len(lst)):
                if i < highest: # female
                    female_n = lst[i].strip()
                    if female_n in female_d:
                        female_d[female_n] += highest - i
                    else:
                        female_d[female_n] = highest - i
                else:  # male
                    male_n = lst[i].strip()
                    if male_n in male_d:
                        male_d[male_n] += len(lst) - i
                    else:
                        male_d[male_n] = len(lst) - i
        all_d['male'] = male_d
        all_d['female'] = female_d
    return all_d


# Problem 4 A
def contains(bst, val):
    if not bst: # if bst is not None
        return False
    else:
        if bst.val == val:
            return True
        elif bst.val > val:
            return contains(bst.left, val)
        else:
            return contains(bst.right, val)


# Problem 4 B
def balanced_brackets(s):
    helper(s, [])


def helper(s, stack):
    if len(s) == 0:
        if len(stack) != 0:
            return False
        else:
            return True
    else:
        ch = s[0]
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
        return helper(s[1:], stack)

# Problem 5 is LC24
def swap_pairs(self, head):
    dummy = ListNode(next=head)
    cur = head
    pre = dummy
    while cur is not None and cur.next is not None:
        pre.next = cur.next
        cur.next = pre.next.next
        pre.next.next = cur
        pre = cur
        cur = cur.next
    return dummy.next


