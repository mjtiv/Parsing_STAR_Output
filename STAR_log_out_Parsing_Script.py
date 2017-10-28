#!/usr/bin/env python3.6
import os

#Program Name: STAR_Output Parsing Program
#Created by M. Joseph Tomlinson IV

#This program parses through STAR Output results and consolidates everything into a tab delimited file
#making examining the data in excel much easier and more accurate then manually curating the data
#a user supplies the parameter file of specific file names and pathways of interest and the
#goes out and retrieves all the data and properly parses it for analysis


#################Global Variables for Program##########################

#Creates the tabs at the top of the STAR tab delimitied text file
file_Tabs="Sample Name\tNumber of input reads\tAverage input read length\tUniquely mapped reads number\t"\
           "Uniquely mapped reads %\tAverage mapped length\tNumber of splices: Total\t"\
           "Number of splices: Annotated (sjdb)\tNumber of splices: GT/AG\tNumber of splices: GC/AG\t"\
           "Number of splices: AT/AC\tNumber of splices: Non-canonical\tMismatch rate per base, %\t"\
           "Deletion rate per bases\tDeletion average length\tInsertion rate per base"\
           "\tInsertion average length\t"\
           "Number of reads mapped to multiple loci\t% of reads mapped to multiple loci\t"\
           "Number of reads mapped to too many loci\t% of reads mapped to too many loci\t"\
           "% of reads unmapped: too many mismatches\t% of reads unmapped: too short\t"\
           "% of reads unmapped: other\tNumber of chimeric reads\t% of chimeric reads \n"

################Program Functions######################################

#Definition splits the line based on the tab
#to retrieve the data from the file (data is tab-delimited)
def split_variables(line):
    line_variables=line.split("\t")
    data=line_variables[1]
    return (data)

#Splits the directory name to retrieve the sample name
def parse_sample_name(directory_step):
    splitting_name=directory_step.split("_Stats")
    name=splitting_name[0]
    return (name)

#Getting all important lines from file--variables follow name of file exactly---tons of variables
def parsing_log_files(file_contents, sample_name):

    number_of_input_reads_line=file_contents[5]
    number_of_input_reads=split_variables(number_of_input_reads_line)

    average_input_read_length_line=file_contents[6]
    average_input_read_length=split_variables(average_input_read_length_line)

    uniquely_mapped_reads_number_line=file_contents[8]
    uniquely_mapped_reads_number=split_variables(uniquely_mapped_reads_number_line)

    uniquely_mapped_reads_percent_line=file_contents[9]
    uniquely_mapped_reads_percent=split_variables(uniquely_mapped_reads_percent_line)
        
    average_mapped_length_line=file_contents[10]
    average_mapped_length=split_variables(average_mapped_length_line)

    number_of_splices_total_line=file_contents[11]
    number_of_splices_total=split_variables(number_of_splices_total_line)

    number_of_splices_annotated_sjdb_line=file_contents[12]
    number_of_splices_annotated_sjdb=split_variables(number_of_splices_annotated_sjdb_line)

    number_of_splices_GT_AG_line=file_contents[13]
    number_of_splices_GT_AG=split_variables(number_of_splices_GT_AG_line)

    number_of_splices_GC_AG_line=file_contents[14]
    number_of_splices_GC_AG=split_variables(number_of_splices_GC_AG_line)

    number_of_splices_AT_AC_line=file_contents[15]
    number_of_splices_AT_AC=split_variables(number_of_splices_AT_AC_line)
        
    number_of_splices_non_canonical_line=file_contents[16]
    number_of_splices_non_canonical=split_variables(number_of_splices_non_canonical_line)

    mismatch_rate_per_base_percent_line=file_contents[17]
    mismatch_rate_per_base_percent=split_variables(mismatch_rate_per_base_percent_line)

    deletion_rate_per_base_line=file_contents[18]
    deletion_rate_per_base=split_variables(deletion_rate_per_base_line)

    deletion_average_length_line=file_contents[19]
    deletion_average_length=split_variables(deletion_average_length_line)

    insertion_rate_per_base_line=file_contents[20]
    insertion_rate_per_base=split_variables(insertion_rate_per_base_line)

    insertion_average_length_line=file_contents[21]
    insertion_average_length=split_variables(insertion_average_length_line)

    number_of_reads_mapped_to_multiple_loci_line=file_contents[23]
    number_of_reads_mapped_to_multiple_loci=split_variables(number_of_reads_mapped_to_multiple_loci_line)

    percent_of_reads_mapped_to_multiple_loci_line=file_contents[24]
    percent_of_reads_mapped_to_multiple_loci=split_variables(percent_of_reads_mapped_to_multiple_loci_line)

    number_of_reads_mapped_to_too_many_loci_line=file_contents[25]
    number_of_reads_mapped_to_too_many_loci=split_variables(number_of_reads_mapped_to_too_many_loci_line)

    percent_of_reads_mapped_to_too_many_loci_line=file_contents[26]
    percent_of_reads_mapped_to_too_many_loci=split_variables(percent_of_reads_mapped_to_too_many_loci_line)

    percent_of_reads_unmapped_too_many_mismatches_line=file_contents[28]
    percent_of_reads_unmapped_too_many_mismatches=split_variables(percent_of_reads_unmapped_too_many_mismatches_line)

    percent_of_reads_unmapped_too_short_line=file_contents[29]
    percent_of_reads_unmapped_too_short=split_variables(percent_of_reads_unmapped_too_short_line)

    percent_of_reads_unmapped_other_line=file_contents[30]
    percent_of_reads_unmapped_other=split_variables(percent_of_reads_unmapped_other_line)
        
    number_of_chimeric_reads_line=file_contents[32]
    number_of_chimeric_reads=split_variables(number_of_chimeric_reads_line)

    percent_of_chimeric_reads_line=file_contents[33]
    percent_of_chimeric_reads=split_variables(percent_of_chimeric_reads_line)
        
    #Combining all the results in a final line for file everything is tab delimited
    all_data=sample_name + "\t" + number_of_input_reads + "\t" + average_input_read_length + "\t"\
              + uniquely_mapped_reads_number + "\t" + uniquely_mapped_reads_percent + "\t"\
              + average_mapped_length + "\t" + number_of_splices_total + "\t" + number_of_splices_annotated_sjdb +\
              "\t" + number_of_splices_GT_AG + "\t" + number_of_splices_GC_AG + "\t" + number_of_splices_AT_AC +\
              "\t" + number_of_splices_non_canonical + "\t" + mismatch_rate_per_base_percent + "\t" +\
              deletion_rate_per_base + "\t" + deletion_average_length + "\t" + insertion_rate_per_base +\
              "\t" + insertion_average_length + "\t" + number_of_reads_mapped_to_multiple_loci + "\t" +\
              percent_of_reads_mapped_to_multiple_loci + "\t" + number_of_reads_mapped_to_too_many_loci + "\t" +\
              percent_of_reads_mapped_to_too_many_loci + "\t" +\
              percent_of_reads_unmapped_too_many_mismatches + "\t" + percent_of_reads_unmapped_too_short + "\t" +\
              percent_of_reads_unmapped_other + "\t" +\
              number_of_chimeric_reads + "\t" + percent_of_chimeric_reads + "\t" + '\n'
    return (all_data)


def read_parameter_file (input_file):
    file_parameters=[line.strip() for line in input_file]

    #Retrieve all the various lines of input (keys and values)---need to get just input parameters
    input_line_1=file_parameters[1]
    input_line_2=file_parameters[2]
    input_line_5=file_parameters[5]

    #Split the key, value pairs of information from the parameter file
    first_pass_file_name = split_variables(input_line_1)
    second_pass_file_name = split_variables(input_line_2)
    directories = split_variables(input_line_5)
    return(first_pass_file_name, second_pass_file_name, directories)


def main():
    
    #Opens the parameter file to get all the required inputs for the rest of the code
    input_file = open('Input_Parameter_File.txt', 'r') #Open the file in python
    parameters=read_parameter_file(input_file) #Definition to parse through a file for parameters
    input_file.close() ####Close the intial file

    #Retrieving the parameters from the parameter file parsing output
    first_pass_file_name=parameters[0]
    second_pass_file_name=parameters[1]
    directories=parameters[2]
    list_of_parsing_directories=directories.split(" ")
    print (list_of_parsing_directories)


    ######Creating texts file to put data into##############
    star_First_Pass_File=open("STAR_First_Pass.txt","w")
    star_Second_Pass_File=open("STAR_Second_Pass.txt","w")

    #####Creating Header for STAR Outputs, this includes all headers for statistical analysis
    star_First_Pass_File.write(file_Tabs)
    star_Second_Pass_File.write(file_Tabs)

    #Two For loops to loop through all the directories of interest to retrieve all the information
    #Starts to loop through the pathways of folders given in parameter program
    for i in range (len(list_of_parsing_directories)):
        print ("this is the first directory being parsed")
        print (list_of_parsing_directories[i])
        directory_pathway=list_of_parsing_directories[i]
        print ("List of sub-directories in the file")
        directory_list=[d for d in os.listdir(list_of_parsing_directories[i]) if os.path.isdir(os.path.join(list_of_parsing_directories[i],d))] #Code from comment 1. http://stackoverflow.com/questions/7781545/how-to-get-all-folder-only-in-a-given-path-in-python
        print (directory_list)
        #Loop searches through the directories and retrieves all the data from the various sub-directories
        for i in range(len(directory_list)):
            print (directory_list[i])
            #Retrieves the directory name
            directory_step=(directory_list[i])
            #Parsing the directory name to get the sample name
            sample_name=parse_sample_name(directory_step)
            print (sample_name)
            #Changes the directory of the program to go inside the sample directory
            new_directory=directory_pathway + "/" + directory_step
            print ("this is the new directory steps being explored")
            print (new_directory)

            os.chdir=(new_directory)
            print (os.chdir)
            file_list=os.listdir(new_directory)
            #print (file_list)

            #Retrieving Information in 1st Pass Log File
            first_pass_log_file=new_directory + "/" + first_pass_file_name
            #Opening file
            file_Step_1_Log_file = open(first_pass_log_file,'r')
            #Importing all the data from the file 
            file_contents=[line.strip() for line in file_Step_1_Log_file]
            #Parsing the file
            parsed_Data=parsing_log_files(file_contents, sample_name)
            #Writing parsed data to first log file
            star_First_Pass_File.write(parsed_Data)
            #Closing the first pass log file
            file_Step_1_Log_file.close()

            #Retrieving Information in 2nd Pass Log File
            second_pass_log_file=new_directory + "/" + second_pass_file_name
            #Opening file
            file_Step_2_Log_file = open(second_pass_log_file,'r')
            #Importing all the data from the file 
            file_contents=[line.strip() for line in file_Step_2_Log_file]
            #Parsing the file
            parsed_Data=parsing_log_files(file_contents, sample_name)
            #Writing parsed data to first log file
            star_Second_Pass_File.write(parsed_Data)
            #Closing the first pass log file
            file_Step_1_Log_file.close()
            
    #Closing all the new files
    star_First_Pass_File.close() ###Closing the 1st STAR Pass Stats file
    star_Second_Pass_File.close() ###Closing the 2nd STAR Pass Stats file

main()






