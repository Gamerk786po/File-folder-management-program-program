# File and Folder management program
# Importing os module
import os
# Importing shutil module
import shutil as shu
#  Functions
# 1 - Create a new folder
def make_a_new_folder(directory_name):
    # Exception handling
    try:
        # Making folder
        os.mkdir(directory_name)
        print(f"The folder {directory_name} have been created.")
    except FileExistsError:
        print(f"The file exists error occured!!!The folder {directory_name} already exists.")
    except OSError as o:
        print(f"The error {o} occured!!!")
    except Exception as e:
        print(f"The error {e} occured!!!")
# 2 - Create multiple folders
def make_multiple_folders(folders_number,directories_name):
    try:
        # Running for loop for creating multiple number of folders
        for i in range(1,folders_number+1):
        # Creating multiple folders
            os.mkdir(f"{directories_name}{i}")
            print(f"The {directories_name}{i} have been created.")
    except FileExistsError:
        print(f"The file exists error occured!!!The folder {directory_name} already exists.")
    except OSError as o:
        print(f"The error {o} occured!!!")
    except Exception as e:
        print(f"The error {e} occured!!!")
# 3 - Create single file
def make_single_file(file_name): 

    try:
        # Creating a single file
        with open(file_name,"w") as file:
            file.write("It is a file created by folder/file management program")
        print(f"The file {file_name} has been created.")
    except FileExistsError:
        print(f"The file exists error occured!!! The file {file_name} already exists.")
    except Exception as e:
        print(f"The error {e} occured!!!")
# 4 - Create multiple files
def make_multiple_files(files_name,files_number):
    try:
        # Running for loop for making multiple files
        for i in range(1,files_number+1):
            # Modifing file names
            files_names=f"{files_name}{i}"
            # creating
            with open(files_names,"w") as file:
                file.write("It is a file created by folder/file management program.")
            print(f"The file {files_names} has been created")
    except FileExistsError:
        print(f"The file exists error occured!!! The file {files_names} already exists.")
    except Exception as e:
        print(f"The error {e} occured!!!")
# 5 - Open a file
def open_a_file(file_name):
    # Exceptional handling
    try:
        os.startfile(file_name)
    except FileNotFoundError:
        print(f"The file {file_name} does not exists.Plz check the path you have given.")
    except OSError as o:
        print(f"The error {o} has occured!!! ")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# 6 - Change path
def change_path(path_ch):
    # Exception handling
    try:
        os.chdir(path_ch)
    except FileNotFoundError:
        print("The given path is incorrect.")
    except OSError as o:
        print(f"The error {o} has occured!!!")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# 7 - Content of folder
def content_folder(folder_name):
    # Exception handling
    try:
        # Making list of folder content
        Folder_content=os.listdir(folder_name)
        print(f"The content of {folder_name} is: ")
        # Using for loop for print all the items of list
        for items in Folder_content:
            print(items)
    except FileNotFoundError:
        print(f"The file {folder_name} does not exists.Plz check the path you have given.")
    except OSError as o:
        print(f"The error {o} has occured!!!")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# 8 - Delete a folder
def delete_folder(folder_name):
    # Exception handling
    try:
        # Deleting as entire folder
        shu.rmtree(folder_name)
        print(f"The folder {folder_name} has been deleted.")
    except FileNotFoundError:
        print(f"The file {folder_name} does not exists.Plz check the path you have given.")
    except OSError as o:
        print(f"The error {o} has occured!!!")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# 9 - Delete a file
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"The file {file_name} has been deleted.")
    except FileNotFoundError:
        print(f"The file {file_name} does not exists.Plz check the path you have given.")
    except OSError as o:
        print(f"The error {o} has occured!!!")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# 10 - Copy file
def copy_folder(folder_name,targated_path):
    try:
        Ok_target=os.path.join(targated_path,folder_name)
        shu.copytree(folder_name,Ok_target,dirs_exist_ok=True)
        print(f"The folder {folder_name} has been copied sucessfully to targated path.")
    except FileNotFoundError:
        print(f"The file {folder_name} does not exists.Plz check the path you have given.")
    except OSError as o:
        print(f"The error {o} has occured!!!")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# 11 - copy file
def copy_file(file_name,targated_path):
    try:
        Ok_target=os.path.join(targated_path,file_name)
        shu.copy(file_name,Ok_target)
        print(f"The file {file_name} has been copied sucessfully to targated path.")
    except FileNotFoundError:
        print(f"The file {file_name} does not exists.Plz check the path you have given.")
    except OSError as o:
        print(f"The error {o} has occured!!!")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# 12 - cut file/folder
def cut_file_folder(folder_and_file_name,targated_path):
    try:
        Ok_target=os.path.join(targated_path,folder_and_file_name)
        shu.move(folder_and_file_name,Ok_target)
        print(f"The file/folder {folder_and_file_name} has been moved succesfully to targated path.")
    except FileNotFoundError:
        print(f"The file/folder {folder_and_file_name} does not exists.Plz check the path you have given.")
    except OSError as o:
        print(f"The error {o} has occured!!!")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# 13 - rename file/folder
def rename_file_folder(old_name,new_name):
    try:
        os.rename(old_name,new_name)
        print(f"The {old_name} has been renamed to {new_name}.")
    except FileNotFoundError:
        print(f"The file/folder {old_name} does not exists.Plz check the path you have given.")
    except OSError as o:
        print(f"The error {o} has occured!!!")
    except Exception as e:
        print(f"The error {e} has occured!!!")
# greatings
print("WELCOME TO FILE/FOLDER MANAGEMENT PROGRAM...")
# Exception handing
try:
    # Taking path from user
    Path=input("Enter the path: ")
    # Running while loop for an infinite loop
    os.chdir(Path)
except FileNotFoundError:
    print("The given path is incorrect.")
while True:
    # Doing exception handling using try/except
    try:
        # Current path
        print(f"Your curent path is {os.getcwd()}")      
        # options
        print("What do you want to do :")
        print("\t 1- Make a new file/folder")
        print("\t 2- Open a file")
        print("\t 3- Copy,cut or rename file/folder")
        print("\t 4- Change the path")
        print("\t 5- View the content of a folder")
        print("\t 6- Delete a file/folder")
        print("\t 0- Exit Program ")
        # Taking the input of his option from the user
        main_option=int(input("Enter your desired option's number: "))
        # Conditions
        # Option - 1
        if main_option == 1:
            # Exception handling for create_option
            try:
                # Options inside main op - 1
                print("What do u want to create: ")
                print("\t 1 - Create Folders")
                print("\t 2 - Create Files")
                # taking input from user for Create option
                create_option=int(input("Enter the number of your desired number: "))
                # Conditions of create options
                if create_option == 1:
                    # Exception handling for folder option
                    try:
                        print("What do u want to create: ")
                        print("\t 1 - Create a single Folder")
                        print("\t 2 - Create multiple folders")
                        option_folder=int(input("Enter the number of your desired option: "))
                        # Conditions of folder creation
                        # Creation of single folder
                        if option_folder == 1:
                            directory_name=input("Enter the name of folder you want to create: ")
                            make_a_new_folder(directory_name)
                        elif option_folder == 2:
                            folders_number=int(input("Enter how many folders you want to make: "))
                            directories_name=input("Enter the name of Folders : ")
                            make_multiple_folders(folders_number,directories_name)
                        else:
                            print("Plz an integer between 1 and 2.")
                    # In case of value error
                    except ValueError:
                        print("The value error occured.")
                        print("Plz enter an integer.")
                    # In case of any error except value error
                    except Exception as e:
                        print(f"The error {e} occured.")
                elif create_option ==2:
                    try:
                        print("What do u want to create: ")
                        print("\t 1 - Create a single File")
                        print("\t 2 - Create multiple files")
                        option_file=int(input("Enter the number of your desired option: "))
                        # Conditions of file creation
                        # Creation of single file
                        if option_file == 1:
                            file_name=input("Enter the file name: ")
                            make_single_file(file_name)
                        # Creation of multiple files
                        elif option_file == 2:
                            files_number=int(input("Enter how many files you want to make: "))
                            files_name=input("Enter the name of files: ")
                            make_multiple_files(files_name,files_number)
                    # In case of value error
                    except ValueError:
                        print("The value error occured.")
                        print("Plz enter an integer.")
                    # In case of any error except value error
                    except Exception as e:
                        print(f"The error {e} occured.")                  
                else:
                    print("Plz enter an integer between 1 and 2")
            # In case of value error
            except ValueError:
                print("The Value error occured!!!.")
                print("Plz enter an integer.")
            # In case of any error except value error
            except Exception as e :
                print(f"An error {e} occured!!!")
        # Option - 2
        elif main_option==2:
            # Taking input from user for file name he/she wants to open
            file_name=input("Enter the name of the file you want to open: ")
            # Open file function
            open_a_file(file_name)
        # Option - 3
        elif main_option ==3:
            try:
                print("What do you want to do:")
                print("\t 1- Copy file/folder")
                print("\t 2- Cut file/folder")
                print("\t 3- Rename file/folder")
                # Taking input
                copy_cut_rename=int(input("Enter your desired number option: "))
                # Copy_delete_cut option conditions
                # option 1
                if copy_cut_rename == 1:
                    print("What do you want to do:")
                    print("\t 1- Copy folder")
                    print("\t 2- Copy file")
                    copy_option=int(input("Enter your desired number option: "))
                    #  Conditions inside option 1 
                    # Option 1
                    if copy_option == 1:
                        folder_name=input("Enter the name of folder: ")
                        targated_path=input("Enter the targated path: ")
                        copy_folder(folder_name,targated_path)
                    # option 2
                    elif copy_option == 2:
                        file_name=input("Enter the name of folder: ")
                        targated_path=input("Enter the targated path: ")
                        copy_file(file_name,targated_path)
                    else:
                        print("Plz enter an integer between 1 and 2")
                # option 2
                elif copy_cut_rename == 2:
                    # Taking input from user for cut function
                    folder_and_file_name=input("Enter the name of file/folder: ")
                    targated_path=input("Enter the targated path: ")
                    # cut file/folder function
                    cut_file_folder(folder_and_file_name,targated_path)
                # option 3
                elif copy_cut_rename == 3:
                    old_name=input("Enter the name of file/folder: ")
                    new_name=input("Enter the new name of file/folder: ")
                    rename_file_folder(old_name,new_name)
                else:
                    print("Plz enter an integer between 1 and 3.")
            except ValueError:
                print("The value error occured!!! plz enter an integer.")
            except Exception as e:
                print(f"The error {e} has occured!!!")        
        
        #  option - 4 
        elif main_option == 4:
            # Taking input from user for
            path_ch=input("Enter the new path: ")
            # Change path function
            change_path(path_ch)
            print(f"The new path is {path_ch}")
        # option - 5
        elif main_option == 5:
            # Taking input from user for folder name
            folder_name=input("Enter the name of folder: ")
            # List content folder
            content_folder(folder_name)
        # option - 6
        elif main_option == 6:
            # Exception handling
            try:
                print("What do you want to delete: ")
                # Delete options
                print("\t 1 - Delete a folder ")
                print("\t 2 - Delete a file ")
                # Taking input from user for Delete option
                delete_option=int(input("Enter the number of your desired option: "))
                # Conditions
                # Delete option 1
                if delete_option == 1:
                    # Taking input form user for folder name
                    folder_name=input("Enter the name of folder: ")
                    delete_folder(folder_name)
                # Delete option 2
                elif delete_option == 2:
                    # Taking input from user for file name
                    file_name=input("Enter the name of file: ")
                    # delete a file function
                    delete_file(file_name)
                else:
                    print("Plz enter an integer between 1 and 2.")
            except ValueError:
                print("The value error occured!!! plz enter an integer.")
            except Exception as e:
                print(f"The error {e} occured!!!")
        elif main_option == 0:
            break
        else:
            print("Plz enter correct option.")
    # In case of Value error
    except ValueError:
        print("The value error occured!!!.")
        print("Plz enter an integer.")
    # In case of os error
    except OSError as o:
        print(f"The error {o} has occured!!!")
    # In case of any error except value error
    except Exception as e :
        print(f"An error {e} occured!!!")
print("The program has ended thank you. ")
