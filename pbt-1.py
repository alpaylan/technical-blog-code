def dummy_sort(l):
		return []
  
  
  
def sort_test_1():
		l = [2, 1, 3, 4]
		sorted_l = dummy_sort(l)
		assert sorted_l == [1, 2, 3, 4]
    

def is_sorted(candidate_list):
		if len(candidate_list) == 0:
				return True
		pivot = candidate_list[0]
		for item in candidate_list:
				if pivot > item:
						return False
				else:
						pivot = item
		return True
    
def sort_test_prop_1():
		l = [2, 1, 3, 4]
		sorted_l = dummy_sort(l)
		assert is_sorted(sorted_l)

    
def elements_same(l1, l2):
		return set(l1) == set(l2)
  

def sort_test_prop_2():
		l = [2, 1, 3, 4]
		sorted_l = dummy_sort(l)
		assert is_sorted(sorted_l) and elements_same(l, sorted_l)
    
def sort_test_prop_3():
		l = [2, 2, 1, 3, 4]
		sorted_l = dummy_sort(l)
		assert is_sorted(sorted_l) and elements_same(l, sorted_l)

def dummy_sort2():
		return [1, 2, 3, 4]


  
  
def is_permutation(l1, l2):
		for item in l1:
				if item in l2:
						l2.remove(item)
				else:
						return False
		return len(l2) == 0
  
def sort_test_prop_4():
		l = [2, 2, 1, 3, 4]
		sorted_l = dummy_sort(l)
		assert is_sorted(sorted_l) and is_permutation(l, sorted_l)
    
    
def sort_test_prop_5():
		l = [2, 2, 1, 3, 4]
		dummy_sorted_l = dummy_sort(l)
		fancy_sorted_l = fancy_sort(l)
		assert dummy_sort(l) == fancy_sort(l)
    
def test_fancy_sort(l):
		dummy_sorted_l = dummy_sort(l)
		fancy_sorted_l = fancy_sort(l)
		assert dummy_sort(l) == fancy_sort(l)

def test_many_cases():
	list_of_cases = [
		[],
		[1],
		[2, 1],
		[3, 1, 2],
		[5, 1, 2, 4]
	]
	for case in list_of_cases:
			test_fancy_sort(case)


def test_many_cases_smart():
		for _ in range(1000):	
				case = generate_test_case_for_sorting()
				test_fancy_sort(case)
        

def generate_test_case_for_sorting_smarter(size):
		actual_size = math.log(size, 2)
		generated_list = []
		for _ in range(actual_size):
				generated_list.append(random.randint(-5, 10000))
		return generated_list

  

def shrink_failing_case(case):
		shrinked_case = case[1:]
		if test_fancy_sort(shrinked_case) == "Fail":
				return shrink_failing_case(shrinked_case)
		else:
				return case
      

def test_many_cases_even_smarter():
		for i in range(1000):	
				case = generate_test_case_for_sorting_smarter(i)
				if test_fancy_sort(case) == "Fail":
						return shrink_failing_case(case)


