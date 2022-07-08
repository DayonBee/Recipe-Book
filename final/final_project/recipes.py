from tkinter import *
import sqlite3

splash_root = Tk()
splash_root.title("The 3 Ingredient Recipe Book")
splash_root.geometry("600x600")
bg = PhotoImage(file = "/Users/dayonbrower/Desktop/final/final_project/cocky.png")
picture_label = Label(splash_root, image=bg)
picture_label.place(x=0, y=0, relwidth=1, relheight=1)

#For main screen
root = Tk()
root.title("The 3 Ingredient Recipe Book")
root.geometry("600x600")
#bg = PhotoImage(file = "/Users/dayonbrower/Desktop/final/final_project/get_cocky.png")
#picture_label = Label(root, image=bg)
#picture_label.place(x=0, y=0, relwidth=1, relheight=1)


#/Users/dayonbrower/Desktop/final/final_project/get_cocky.png

#Making the Database
conn = sqlite3.connect('recipe_book.db')

c = conn.cursor()

#Making the table
#c.execute("""CREATE TABLE recipes(
#        recipe_name text,
#        first_ingredient text,
#        second_ingredient text,
#        third_ingredient text
#)""")

#Create function to delete a recipe
def delete():
    conn = sqlite3.connect('recipe_book.db')
    c = conn.cursor()

    c.execute("DELETE from recipes WHERE oid= " + delete_recipe.get())

    delete_recipe.delete(0,END)

    conn.commit()
    conn.close()


#Create function for submit button
def submit():
    conn = sqlite3.connect('recipe_book.db')
    c = conn.cursor()

    #This Inserts the values into the table
    c.execute("INSERT INTO recipes VALUES (:recipe, :first_ingredient, :second_ingredient, :third_ingredient)",
            {
                'recipe': recipe.get(),
                'first_ingredient': first_ingredient.get(),
                'second_ingredient':second_ingredient.get(),
                'third_ingredient': third_ingredient.get()
            })

    recipe.delete(0,END)
    first_ingredient.delete(0,END)
    second_ingredient.delete(0,END)
    third_ingredient.delete(0,END)


    conn.commit()
    conn.close()


#Create function for show all button
def query():
    conn = sqlite3.connect('recipe_book.db')
    c = conn.cursor()
#oid is like the number for each recipe you can use the oid later to delete as well
    c.execute("SELECT * , oid FROM recipes")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[4]) + "." + " " + str(record[0]) + ": " + str(record[1]) + ", " + str(record[2]) + ", " + str(record[3]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2 )

    conn.commit()
    conn.close()


#This Creates Text Boxes
recipe = Entry(root,width = 30)
recipe.grid(row=0, column=1,padx=20, pady=(20,0))
first_ingredient = Entry(root,width = 30)
first_ingredient.grid(row=1, column=1,padx=20)
second_ingredient = Entry(root,width = 30)
second_ingredient.grid(row=2, column=1,padx=20)
third_ingredient = Entry(root,width = 30)
third_ingredient.grid(row=3, column=1,padx=20)
delete_recipe = Entry(root,width=30)
delete_recipe.grid(row=6, column=1)


#This creates labels for the text boxes
recipe_label = Label(root, text="Recipe Name",bg='#800020', fg='#EDCE67')
recipe_label.grid(row=0,column=0, pady=(20,0))
first_label = Label(root, text="First Ingredient",bg='#800020', fg='#EDCE67')
first_label.grid(row=1,column=0)
second_label = Label(root, text="Second Ingredient",bg='#800020', fg='#EDCE67')
second_label.grid(row=2,column=0)
third_label = Label(root, text="Third Ingredient",bg='#800020', fg='#EDCE67')
third_label.grid(row=3,column=0)
delete_label = Label(root, text="Enter Recipe Number",bg='#800020', fg='#EDCE67')
delete_label.grid(row=6,column=0)

#This will add the recipe to the "Book"
add_btn = Button(root,text="Add Recipe to the Book", command=submit,fg='#800020')
add_btn.grid(row=4, column=0, columnspan=2, pady=10,padx=10, ipadx=135)


#This will show all recipes in the "Book"
showall_btn = Button(root,text="Show all Recipes in the Book", command=query, fg='#800020')
showall_btn.grid(row=5, column=0, columnspan=2, pady=10,padx=10, ipadx=135)

#This will allow the user to delete a recipe
delete_btn = Button(root,text="Erase a Recipe From the Book", command=delete, fg='#800020')
delete_btn.grid(row=7, column=0, columnspan=2, pady=10,padx=10, ipadx=135)


conn.commit()

conn.close()



root.mainloop()