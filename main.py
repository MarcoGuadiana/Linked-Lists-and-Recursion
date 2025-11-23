from linked_list import LinkedList

if __name__ == "__main__":
    print("--- Linked List Demonstration ---")
    
    my_list = LinkedList()
    print("1) Created an empty list.")

    my_list.insert_at_front(15)
    my_list.insert_at_end(30)
    my_list.insert_at_front(5)
    my_list.insert_at_end(50)
    print("2) Inserted data: 5, 15, 30, 50.")

    print("3) Current List:")
    my_list.display()
    
    print("---------------------------------")
    
    total_sum = my_list.recursive_sum()
    print(f"4) Recursive Sum: {total_sum}")

    target_found = 30
    target_missing = 99
    
    found_result = my_list.recursive_search(target_found)
    missing_result = my_list.recursive_search(target_missing)
    
    print(f"5a) Recursive Search for {target_found}: {found_result}")
    print(f"5b) Recursive Search for {target_missing}: {missing_result}")
    
    print("---------------------------------")

    print("6) Reversing the list...")
    my_list.recursive_reverse()
    
    print("   Reversed List:")
    my_list.display()
    print("--- Demonstration Complete ---")