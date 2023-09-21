/* 
* structure that contains all of the releveant fields for the arguments/filters in flight data file
*/
struct airline_struct {
    char airline_name[50];
    char airline_icao_unique_code[50];
    char airline_country[50];
    char from_airport_name[50];
    char from_airport_city[50];
    char from_airport_country[50];
    char from_airport_icao_unique_code[50];
    float from_airport_altitude;
    char to_airport_name[50];
    char to_airport_city[50];
    char to_airport_country[50];
    char to_airport_icao_unique_code[50];
    float to_airport_altitude;
};

void get_command_line(int argc, char *argv[]);
void open_files_and_case_check(char *titles_array[], char *data_array[]);
void which_case(char *titles[], char *data[], FILE *flight_info, FILE *output);
void close_files(FILE *flight_info, FILE *output);
void check_counters(int found_counter_case1, int found_counter_case2, int found_counter_case3, FILE *output);
int case_one_output(int found_counter_case1, FILE *output, struct airline_struct info);
int case_two_output(int found_counter_case2, FILE *output, struct airline_struct info);
int case_three_output(int found_counter_case3, FILE *output, struct airline_struct info);

/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int main(int argc, char *argv[])
{
    get_command_line(argc, argv);
    exit(0);
}

/**
 * Function: get_command_line
 * --------------
 * @brief Parsing through the command line to gather and categorize relevant information
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return None
 *
 */
void get_command_line(int argc, char *argv[]) {
    if (argc == 1) {
        exit(1);
    }
    char *titles[10];
    char *data[10];

    for(int i = 1; i < argc; i++) {

        strtok(argv[i], "=");
        data[i] = strtok(NULL, "=");
        titles[i] = strtok(argv[i], "--");    
    }
    open_files_and_case_check(titles, data);
}

/**
 * Function: open_files_and_case_check
 * --------------
 * @brief Opening necessary files so we are able to read/write and passing file pointers to helper function that handles cases
 *
 * @param titles Array of headers/titles found in the command line input
 * @param data Array of strings/data given in the command line input
 * @return None
 *
 */
void open_files_and_case_check(char *titles[], char *data[]) {
    FILE *flight_info;
    flight_info = fopen(data[1], "r");

    FILE *output;
    output = fopen("output.txt", "w");

    which_case(titles, data, flight_info, output);
    close_files(flight_info, output);
}

/**
 * Function: which_case
 * --------------
 * @brief Checking whether the input from the command line requires case 1, case 2, or case 3 output
 *
 * @param titles Array of headers/titles found in the command line input
 * @param data Array of string/data given in the command line input
 * @param flight_info File to read that was opened in open_files_and_case_check (first element in data array)
 * @param output Output file that was opened in open_files_and_case_check to write final output to
 * @return None
 *
 */
void which_case(char *titles[], char *data[], FILE *flight_info, FILE *output) {
    struct airline_struct info;
    
    int check_case1 = strcmp(titles[2], "AIRLINE");
    int check_case2 = strcmp(titles[2], "SRC_COUNTRY");
    int check_case3 = strcmp(titles[2], "SRC_CITY");
    
    char line[1024];
    int found_counter_case1 = 0;
    int found_counter_case2 = 0;
    int found_counter_case3 = 0;
    
    while(fgets(line, 1024, flight_info) != NULL) {
        
        sscanf(line, "%[^,], %[^,], %[^,], %[^,], %[^,], %[^,], %[^,], %f, %[^,], %[^,], %[^,], %[^,], %f", info.airline_name, info.airline_icao_unique_code, info.airline_country, info.from_airport_name, info.from_airport_city, info.from_airport_country, info.from_airport_icao_unique_code, &info.from_airport_altitude, info.to_airport_name, info.to_airport_city, info.to_airport_country, info.to_airport_icao_unique_code, &info.to_airport_altitude);

        if (check_case1 == 0) {
            int check_airline_case1 = strcmp(data[2], info.airline_icao_unique_code);
            int check_dest_case1 = strcmp(data[3], info.to_airport_country);
            if (check_airline_case1 == 0 && check_dest_case1 == 0) {
                found_counter_case1 = case_one_output(found_counter_case1, output, info);
            } 
        } else if(check_case2 == 0) {
            int check_src_case2 = strcmp(data[2], info.from_airport_country);
            int check_dest_city_case2 = strcmp(data[3], info.to_airport_city);
            int check_dest_country_case2 = strcmp(data[4], info.to_airport_country);
                
            if (check_src_case2 == 0 && check_dest_city_case2 == 0 && check_dest_country_case2 == 0) {
                found_counter_case2 = case_two_output(found_counter_case2, output, info);
            }
        } else if(check_case3 == 0) {
            int check_src_city_case3 = strcmp(data[2], info.from_airport_city);
            int check_src_country_case3 = strcmp(data[3], info.from_airport_country);
            int check_dest_city_case3 = strcmp(data[4], info.to_airport_city);
            int check_dest_country_case3 = strcmp(data[5], info.to_airport_country);
            if(check_src_city_case3 == 0 && check_src_country_case3 == 0 && check_dest_city_case3 == 0 && check_dest_country_case3 == 0) {
                found_counter_case3 = case_three_output(found_counter_case3, output, info);
            }
        }
        
    }
    check_counters(found_counter_case1, found_counter_case2, found_counter_case3, output);
}

/**
 * Function: close_files
 * --------------
 * @brief Closes all files that were opened previously in read/write mode
 *
 * @param flight_info File to read that was opened in open_files_and_case_check (first element in data array)
 * @param output Output file that was opened in open_files_and_case_check to write final output to
 * @return None
 *
 */
void close_files(FILE *flight_info, FILE *output) {
    fclose(flight_info);
    fclose(output);
}

/**
 * Function: check_counters
 * --------------
 * @brief Checks counter variables to see if no matches in flight data file were found. If all variables are equal to zero, then no results were found and it writes the appropriate output ("NO RESULTS FOUND.") to the output file.
 *
 * @param found_counter_case1 Integer variable that tracks how many times a line in the flight information data-file matches requirements for case 1 output
 * @param found_counter_case2 Integer variable that tracks how many times a line in the flight information data-file matches requirements for case 2 output
 * @param found_counter_case3 Integer variable that tracks how many times a line in the flight information data-file matches requirements for case 3 output
 * @param output Output file that was opened in open_files_and_case_check to write final output to
 * @return None
 *
 */
void check_counters(int found_counter_case1, int found_counter_case2, int found_counter_case3, FILE *output) {
    if (found_counter_case1 == 0 && found_counter_case2 == 0 && found_counter_case3 == 0) {
        fprintf(output, "%s\n", "NO RESULTS FOUND.");
    }
}

/**
 * Function: case_one_output
 * --------------
 * @brief Prints the appropriate output to the output file (output.txt) for case 1 when called. Uses counter variable to check printing variations.
 *
 * @param found_counter_case1 Integer variable that tracks how many times a line in the flight information data-file matches requirements for case 1 output
 * @param output Output file that was opened in open_files_and_case_check to write final output to
 * @param info airline structure with all of the file arguments/filter fields
 * @return found_counter_case1, counter variable
 *
 */
int case_one_output(int found_counter_case1, FILE *output, struct airline_struct info) {
    if(found_counter_case1 == 0) {
        fprintf(output, "FLIGHTS TO %s BY %s (%s):\nFROM: %s, %s, %s TO: %s (%s), %s\n", info.to_airport_country, info.airline_name, info.airline_icao_unique_code, info.from_airport_icao_unique_code, info.from_airport_city, info.from_airport_country, info.to_airport_name, info.to_airport_icao_unique_code, info.to_airport_city);
        found_counter_case1++;
    } else {
        fprintf(output, "FROM: %s, %s, %s TO: %s (%s), %s\n", info.from_airport_icao_unique_code, info.from_airport_city, info.from_airport_country, info.to_airport_name, info.to_airport_icao_unique_code, info.to_airport_city);
    }
    return found_counter_case1;
}

/**
 * Function: case_two_output
 * --------------
 * @brief Prints the appropriate output to the output file (output.txt) for case 2 when called. Uses counter variable to check printing variations.
 *
 * @param found_counter_case2 Integer variable that tracks how many times a line in the flight information data-file matches requirements for case 2 output
 * @param output Output file that was opened in open_files_and_case_check to write final output to
 * @param info airline structure with all of the file arguments/filter fields
 * @return found_counter_case1, counter variable
 *
 */
int case_two_output(int found_counter_case2, FILE *output, struct airline_struct info) {
    if(found_counter_case2 == 0) {
        fprintf(output, "FLIGHTS FROM %s TO %s, %s:\nAIRLINE: %s (%s) ORIGIN: %s (%s), %s\n", info.from_airport_country, info.to_airport_city, info.to_airport_country, info.airline_name, info.airline_icao_unique_code, info.from_airport_name, info.from_airport_icao_unique_code, info.from_airport_city);
        found_counter_case2++;
    } else {
        fprintf(output, "AIRLINE: %s (%s) ORIGIN: %s (%s), %s\n", info.airline_name, info.airline_icao_unique_code, info.from_airport_name, info.from_airport_icao_unique_code, info.from_airport_city);
    }
    return found_counter_case2;
}

/**
 * Function: case_three_output
 * --------------
 * @brief Prints the appropriate output to the output file (output.txt) for case 3 when called. Uses counter variable to check printing variations.
 *
 * @param found_counter_case3 Integer variable that tracks how many times a line in the flight information data-file matches requirements for case 3 output
 * @param output Output file that was opened in open_files_and_case_check to write final output to
 * @param info airline structure with all of the file arguments/filter fields
 * @return found_counter_case1, counter variable
 *
 */
int case_three_output(int found_counter_case3, FILE *output, struct airline_struct info) {
    if(found_counter_case3 == 0) {
        fprintf(output, "FLIGHTS FROM %s, %s TO %s, %s:\nAIRLINE: %s (%s) ROUTE: %s-%s\n", info.from_airport_city, info.from_airport_country, info.to_airport_city, info.to_airport_country, info.airline_name, info.airline_icao_unique_code, info.from_airport_icao_unique_code, info.to_airport_icao_unique_code);
        found_counter_case3++;
    } else {
        fprintf(output, "AIRLINE: %s (%s) ROUTE: %s-%s\n", info.airline_name, info.airline_icao_unique_code, info.from_airport_icao_unique_code, info.to_airport_icao_unique_code);
    }
    return found_counter_case3;
}
