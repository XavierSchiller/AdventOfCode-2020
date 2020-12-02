#include<iostream>
#include<set>
#include<vector>


int main(){
	std::set<int> input;
	int temp;
	for(int i=0; i<200; i++){
		std::cin >> temp;
		input.insert(temp);
	}

	for(auto i: input){
		int sum = 2020;
		auto it = input.find(sum - i);
		if(it != input.end()){
			std::cout << (*it)*i << std::endl;
			break;	
		}

	}

	int sum = 2020;
	for(auto i: input){
		// Picked the First element. Pick the Second One.
		for (auto j: input){
			//Picked Second element. Search for Missing.
			auto last = input.find(sum - i - j);
			//Check if Exists:

			if(last != input.end()){
				std::cout << (*last)*i*j << " Sum:" << (*last)+i+j << "Elements" << *last << "," << i << "," << j << std::endl;
			}
		}
	}
	return 0;	
		
}
