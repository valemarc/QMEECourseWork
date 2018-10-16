# This loop calculates heights of trees found in the trees.csv file based on the 
# given distance of each tree from its base
# and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# OUTPUT
# The heights of the tree, same units as "distance"

#MyData <- read.csv("../data/trees.csv")
args <- commandArgs(TRUE)
if (length(args) < 1){
  print("No file specified, using default...")
  filetoread <- "../data/trees.csv"
} else {
  filetoread <- args[1]
}

print(filetoread)
print(length(args))
MyData <- read.csv(filetoread)

for(i in MyData) {
  species <- MyData$Species
  degrees <- MyData$Angle.degrees
  distance <- MyData$Distance.m
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  #print(paste("Tree height is:", height))
  dfrm <- data.frame(Species = species, Distance.m = distance, Angle.degrees = degrees, Tree.height.m = height)
  filetoread_m = basename(filetoread)
  filetoread_mod <- tools::file_path_sans_ext("trees.csv")
  OutPath<- "../results/"
  write.csv(data.frame(Species = species, Distance.m = distance, Angle.degrees = degrees, Tree.height.m = height),file = paste0(OutPath,filetoread_mod, "_treeheights.csv"), append=TRUE)
}




