#python #datamanagement 


# Basic Starting Things

#### Opening The EXCEL sheet (.xlsx)

```python
import pandas as pd
from pathlib import Path

file_location = Path("FOLDER FROM DIRECTORY ROOT") / "SUB FOLDER" / "FILENAME.xlsx"
file = pd.read_excel(file_location, header=x)

```

In this example, we import **Pandas** itself, and then *Path* from *pathlib* to help located any files we're handling easier.
Now, "*file*" is what is used to do anything managing the **excel file** (which is now a **DataFrame**).

4. -- reads the **excel file** at the target location defined in *file_location*, starting at the row defined with "*header=x*",  the "*x*" variable being the starting row, and turning it into a **DataFrame** stored in the variable name "*file*".
## Some Basic Functions

#### Basic sheet info functions
```python
file.head(X)
file.columns
file.shape
```

1. -- By default the first 5 rows, with variable passthrough
2. -- the title of the columns as *index object* :**result**: *Index(['Position', 'In', 'Out', 'Hours'], dtype='object')*
3. -- the Height & Length of the sheet :**result**: *(5,4)* :: *(TopToBottom, LeftToRight)*
---
#### The *loc* function
```python
file.loc[ROW, "COLUMN"]
file.loc[STARTING ROW:ENDING ROW, "STARTING COLUMN":"ENDING COLUMN"]
```

The *.loc* function on a file is used for grabbing and setting data in the **excel file**, and other **DataFrame**.

The basic structure is:
- The variable for the excel file: *file*
- The *.loc* function call, with brackets: *file.loc[]*
- Then the label of the row you want to access: *file.loc[row-label]*
- Then the label of the column you want to access: *file.loc[row-label, "column-label"]*
- This can be altered to include a start/end point for either, with a colon.: *file.loc[row1-label:row2-label, "column1-label":"column2-label"]*
- The colon can also be used alone to select all of one: *file.loc[:, "column-label"]*

> [!note] When indexing with **Python Slicing** VS *.loc*
> Unlike **python slicing** `list[1:3]`', using *.loc* `file.loc[1:3]` ==includes the ending value==
> ```python
> print(list[1:3]) ---> 1, 2
> 
> print(file.loc[1:3]) ---> 1, 2, 3
> ```

---
##### Getting Data OUT
When using it to select a data range, it seems to break down the range into items depending on the scope of the range. For example:

```python
          Position       In       Out  Hours
1  Wednesday 01/28      NaN       NaN    NaN
2              QB1  4:00 PM  10:30 PM    6.0
3     Sunday 02/01      NaN       NaN    NaN
4              SSW  5:00 PM   9:00 PM    4.0
```
###### Printing with *.loc*
Given the **DataFrame**, if you print the *.loc* function (``print(file.loc[x,y])``) with these ranges: 
*[1, : ]* :: *[first row, all columns]*, 
*[2, : ]* :: *[second row, all columns]*, 
it'd look like this:

As it's now created a **Series** instead of a **DataFrame**; with the far left being the **Index** (Originally the column titles) and the right becoming the **Values** (Originally the cell values of that row)

If you want the **DataFrame** for that range, use `print(file.loc[[x],y])` instead.
```python
print(file.loc[2,:])

OUTPUT:
	Position         QB1
	In           4:00 PM
	Out         10:30 PM
	Hours            6.0
	Name: 2, dtype: object
	
print(file.loc[[2],:])

OUTPUT:
	Position       In       Out  Hours
2      QB1  4:00 PM  10:30 PM    6.0
```
###### Iterating Through *items* with *.loc*
And when using a *for* loop to cycle through it in terms of *items*, It makes each "cell" in the given row a "item", if you would.
-- As shown bellow:
```python
for item in file.loc[1, :]:
	print(item, type(item))
	
OUTPUT:
	Wednesday 01/28 <class 'str'>
	nan <class 'float'>
	nan <class 'float'>
	nan <class 'numpy.float64'>
```

> [!info] When Iterating through a **DataFrame** with *for item in file.loc[x,y]*
> When using a *for* loop to iterate through a **DataFrame** range, if you have multiple rows ==AND== multiple columns selected, the *items* passed into/iterated through with the loop will be the column titles, as specifying more than one row ==AND== column makes it a **DataFrame** instead of a **Series**. When iterating through a **Series** with this method, the *items* are the *values*, and when it's a **DataFrame** the *items* are the *column labels*.
> ```python
> for item in file.loc[1:2, "Position":"In"]:
>   print(f"Item: {item} | Type: {type(item)}")
> 
> OUTPUT:
> 	Item: Position | Type: <class 'str'>
> 	Item: In | Type: <class 'str'>
> ```

###### Iterating Values in a 2D Selection

Row-Wise
```python
for _, row in file.loc[1:2, "Position":"In"].iterrows():
    print(row["Position"], row["In"])
    
OUTPUT:
	Wednesday 01/28 nan #row 1
	QB1 4:00 PM #row 2
```
Cell-By-Cell
```python
for value in file.loc[1:2, "Position":"In"].to_numpy().flatten():
    print(value)
    
OUTPUT:
	Wednesday 01/28 #row 1, cell 1
	nan #row 1, cell 2
	QB1 #row 2, cell 1
	4:00 PM #row 2, cell 2
```