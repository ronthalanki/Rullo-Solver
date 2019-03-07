#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <set> 
#include <iterator> 

using namespace std;

class Puzzle {
    public:
        //Given
        int size;
        int * row_targets;
        int * col_targets;
        int * nums;

        //Determined
        int * curr_row_totals;
        int * curr_col_totals;
        int * strategy;
};

//converts string of ints into lst of ints
void split(string str, int * output_lst) {
    vector<string> split_strings;
    stringstream ss(str);
    string tok;
    
    while(getline(ss, tok, ',')) {
        split_strings.push_back(tok);
    }

    for (int i = 0; i < split_strings.size(); i++) {
        output_lst[i] = stoi(split_strings[i]);
    }
}

void initialize(string file_name, Puzzle * p) {
    //Read file
    ifstream input_file_stream;
    input_file_stream.open(file_name);
    input_file_stream >> p->size;

    string temp;
    input_file_stream >> temp;
    p->row_targets = (int *) malloc(sizeof(int) * p->size);
    split(temp, p->row_targets);

    input_file_stream >> temp;
    p->col_targets = (int *) malloc(sizeof(int) * p->size);
    split(temp, p->col_targets);

    p->nums = (int *) malloc(sizeof(int) * p->size * p->size);
    for (int i = 0; i < p->size; i++) {
        input_file_stream >> temp;
        split(temp, p->nums + p->size * i);
    }

    //Initialize other lsts
    p->curr_row_totals = (int *) calloc(p->size, sizeof(int));
    p->curr_col_totals = (int *) calloc(p->size, sizeof(int));
    p->strategy = (int *) calloc(p->size, sizeof(int));
}

void cleanup(Puzzle * p) {
    free(p->row_targets);
    free(p->col_targets);
    free(p->nums);
    free(p);
}

//TODO: use special print thing in tutorialspoint
void print_lst(int * lst, int size) {
    for (int i = 0; i < size; i++) {
        cout << lst[i] << "\t";
    }
    cout << endl;
}

void print_puzzle(Puzzle * p) {
    cout << "Size: " << endl << p->size << endl;
    cout << "Row_Targets: " << endl;
    print_lst(p->row_targets, p->size);

    cout << "Col_Targets: " << endl;
    print_lst(p->col_targets, p->size);

    cout << "Nums:" << endl;
    for (int r = 0; r < p->size; r++) {
        print_lst(p->nums + r * p->size, p->size);
    }

    cout << "Curr Row Totals: " << endl;
    print_lst(p->curr_row_totals, p->size);

    cout << "Curr Col Totals: " << endl;
    print_lst(p->curr_col_totals, p->size);
}

void sum_combinations_helper(int lst[], int length, int index, vector<int> &p, int remaining_sum, vector<vector<int>> &combinations) {
    for (int i = index; i < length; i++) {
        int temp = remaining_sum - lst[i];

        if (temp == 0) {
            vector<int> output;
            for (int i = 0; i < p.size(); i++) {
                output.push_back(p[i]);
            }
            output.push_back(lst[i]);
            combinations.push_back(output);
            /*
            for (int i = 0; i < combinations[combinations.size() - 1].size(); i++) {
                cout << combinations[combinations.size() - 1][i] << "\t";
            }
            cout << endl;
            */
        } else if (temp > 0) {
            vector<int> b = p;
            b.push_back(lst[i]);
            sum_combinations_helper(lst, length, i + 1, b, temp, combinations);
        }
    }
}

void sum_combinations(int lst[], int length, int sum) {
    vector<int> p;
    vector<vector<int>> combinations;
    sum_combinations_helper(lst, length, 0, p, sum, combinations);

    //any number that doesn't exist in any of the possible combinations should be removed
    //any number that doesn't have duplicates and exists in all solutions should be definitely yess

    /*
    for (int i = 0; i < combinations.size(); i++) {
        for (int j = 0; j < combinations[i].size(); j++) {
            used_numbers.add(combinations[i][j]);
        }
        cout << endl;
    }
    */
}

//TODO: check if there was a change
void strategy(Puzzle * p) {
    //update curr_totals, then update maybes, yes, and no's accordingly
    for (int r = 0; r < p->size; r++) {
        for (int c = 0; c < p->size; c++) {
            if (p->strategy[r * p->size + c] != 2) {
                p->curr_row_totals[r] += p->nums[r * p->size + c];
            }
        }
    }

    for (int r = 0; r < p->size; r++) {
        for (int c = 0; c < p->size; c++) {
            if (p->strategy[r * p->size + c] != 2) {
                p->curr_col_totals[c] += p->nums[r * p->size + c];
            }
        }
    }
}

main() {
    /*
    Puzzle * p = (Puzzle *) malloc(sizeof(Puzzle));
    initialize("./test-cases/1-sanity-check.txt", p);
    strategy(p);
    print_puzzle(p);

    cleanup(p);
    */
    int sum[] = {8,9,7,6};
    set<int> used_numbers;
    for (int i = 0; i < 4; i++) {
        used_numbers.insert(sum[i]);
    }

    cout << *used_numbers.find(2) << endl;
    cout << *used_numbers.find(9) << endl;
    //sum_combinations(sum, 4, 6);
    return 0; //end program
}
