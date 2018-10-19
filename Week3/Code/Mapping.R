#Load data
GPDD_data <- load("../data/GPDDFiltered.RData")
head(gpdd)

#Load required package
install.packages("maps")
library(maps)

map("world", fill=TRUE, col="white", bg="lightblue", ylim=c(-60, 90), mar=c(0,0,0,0))
points(gpdd$long,gpdd$lat, col="red", pch=16)

###There is a strong geographic bias in the data towards Europe and North America
###There also appear to be a taxonomic bias towards terrestrial mammals and birds