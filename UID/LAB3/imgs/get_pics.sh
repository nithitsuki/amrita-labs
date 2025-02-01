#!/bin/bash

# Create an array with the names of the characters
names=("Koro-sensei" "Kaede Kayano" "Karma Akabane" "Tadaomi Karasuma" "Gakushu Asano" "Itona Horibe" "Kotaro Takebayashi" "Gakuho Asano")

# Create an array with the corresponding image URLs
urls=("https://static.wikia.nocookie.net/assassinationclassroom/images/2/24/Korosensei.png/revision/latest/scale-to-width-down/220?cb=20141224005701"
      "https://static.wikia.nocookie.net/assassinationclassroom/images/0/09/Kaede_Kayano.png/revision/latest/scale-to-width-down/123?cb=20141223225442"
      "https://static.wikia.nocookie.net/assassinationclassroom/images/7/71/Karma_Akabane.png/revision/latest?cb=20141223224512"
      "https://static.wikia.nocookie.net/assassinationclassroom/images/6/61/Tadaomi_Karasuma.png/revision/latest?cb=20141224005549"
      "https://static.wikia.nocookie.net/assassinationclassroom/images/e/e4/Gakushuuchar.png/revision/latest/scale-to-width-down/123?cb=20151223121912"
      "https://static.wikia.nocookie.net/assassinationclassroom/images/1/19/Itonachar.png/revision/latest/scale-to-width-down/123?cb=20151223115424"
      "https://static.wikia.nocookie.net/assassinationclassroom/images/4/48/Kotaro_Takebayashi.png/revision/latest/scale-to-width-down/123?cb=20141223230843"
      "https://www.behindthevoiceactors.com/_img/chars/thumbs/gakuho-asano-assassination-classroom-27.2_thumb.jpg")

asano=()
# Loop over each name and corresponding URL, downloading each image and renaming it
for i in "${!names[@]}"; do
    wget -O "${names[$i]}.jpg" "${urls[$i]}"
done
