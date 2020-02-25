class Terminal_Input:

    start_message = \
        "\n" \
        "Thanks for using the Barren Land Analysis\n" \
        "\n" \
        "Please enter the total land size\n" \
        "Example: 400, 600 \n" \
        "then hit enter"

    land_message = \
        "Please enter for coordinates for the barren land\n" \
        "Example: 0 292 399 307 \n" \
        "Once you are done, type \"Done\""\

    visualization_message = \
        "You would like a visualizations of the result?(y/n)\n" \
        "Note this functionally will currently only work if you are running this locally"\

    def __init__(self):
        self.x, self.y = self.get_plot_size()
        self.coordinates = self.get_barren_coordinates()
        self.visualizations = self.get_visualization_method()
        self.results()

    def get_plot_size(self) -> (int, int):
        print(self.start_message)
        while True:
            try:
                x,y = input().strip().split(", ")
                x, y = int(x), int(y)
                break
            except ValueError:
                print("Sorry that format was incorrect please "
                      "enter the numbers with one space between each number \"x, y\"\n"
                      "Example: 0 292 399 307")
        return x, y

    def get_barren_coordinates(self) -> list:
        print(self.land_message)
        coordinates = []
        while True:
            response = input()
            if response == "Done":
                break
            try:
                response = response.strip()

                coords = [int(x) for x in response.split(" ")]

                if len(coords) != 4:
                    print("Input 4 numbers at one time then hit enter!")
                    raise ValueError

                if not 0 <= coords[0] < self.x or \
                        not 0 <= coords[2] < self.x:
                    print("X value is greater then size of land")
                    raise ValueError

                if not 0 <= coords[1] < self.y or \
                        not 0 <= coords[3] < self.y:
                    print("Y value is greater then size of land")
                    raise ValueError

                coordinates.append(coords)
            except ValueError:
                print("Format wrong here is an of a correct input\n"
                    "Example: 0 292 399 307")
        return coordinates

    def get_visualization_method(self) -> bool:
        print(self.visualization_message)
        while True:
            response = input().lower()
            if response == 'y':
                result = True
                break
            if response == 'n':
                result = False
                break
            else:
                print("Not sure what that means - try again. "
                      "Type \"y\" for yes or \"n\" for no")
        return result


    def results(self):
        print("Results")
        print("The land size is: (" + str(self.x) + ", " + str(self.y)+")")
        print("The barren lands are:")
        for coords in self.coordinates:
            print(coords)


if __name__ == "__main__":
    Terminal_Input()
