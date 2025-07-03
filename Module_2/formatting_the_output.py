# 1. minimize the number of print() function invocations by inserting the \n sequence into the strings
# 2. make the arrow twice as large (but keep the proportions)
# 3. duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
# 4. remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
# 5. do the same with some of the parentheses;
# 6. change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
# 7. replace some of the quotes with apostrophes; watch what happens carefully.

# ORIGINAL
print("ORIGINAL\n")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# 1. minimize the number of print() function invocations by inserting the \n sequence into the strings
print("EXAMPLE 1\n")
print("    *", "   * *", "  *   *", " *     *", sep="\n" )
print("***   ***", "  *   *", "  *   *", "  *****", sep="\n")

# 2. make the arrow twice as large (but keep the proportions)
str_list = ["    *",
            "   * *",
            "  *   *",
            " *     *",
            "***   ***",
            "  *   *",
            "  *   *",
            "  *****"]

print("EXAMPLE 2\n")
for s in str_list:
    new_str = ''
    for char in s:
        new_str += char * 2
    print(new_str, end='\n\n')



