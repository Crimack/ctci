from linked_list import LinkedList

def is_palindrome(linked):
	stack = []
	curr =  fast = linked.head
	while fast is not None and fast.next is not None:
		stack.append(curr.value)
		curr = curr.next
		fast = fast.next.next
	if fast is not None:
		curr = curr.next
	while curr is not None:
		if curr.value != stack.pop():
			print curr.value
			return False
		curr = curr.next
	return True

l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(2)
l.push(1)
print is_palindrome(l)

m = LinkedList()
m.push(1)
m.push(2)
m.push(2)
m.push(1)
print is_palindrome(m)
