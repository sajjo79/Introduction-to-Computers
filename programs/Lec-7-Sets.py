# python set creation it does not support indexing
furniture={"chair","table","sofa","dinning table"}
print(furniture)
#print(furniture[2])

# accessing set elements
print("sofa" in furniture)
furniture.add("bed")
print(furniture)
furniture.update({"study table"})
print(furniture)

# removing an element
furniture.discard("study table")
print(furniture)


