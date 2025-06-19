import cv2
import numpy as np

class mapper:
    def __init__(self, map_image): # map image is a BGR numpy array for cv2 (3D)
        self.map_image_layer = map_image
        self.dissolved_oxygen_sensor_layer = np.full(map_image.shape[:3], 0, dtype=np.uint8)  # Single channel for sensor data. -inf indicates no data
        self.dissolved_oxygen_sensor_mask = np.full(map_image.shape[:2], False, dtype=bool)  # Mask for sensor data points
        self.map = np.zeros(map_image.shape[:3], dtype=np.uint8)
        self.shape = map_image.shape[:3]


    def update_dissolved_oxygen_layer(self, sensor_data, radius=3):
        """
        Add a point of dissolved oxygen sensor data to the map.
        sensor_data: a tuple of ((x,y), data) of a coordinate and the dissolved oxygen value at that coordinate.
        radius: the radius around the sensor data point to inflate the data.
        """
        
        # Inflate the sensor data in a small radius
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                # Check if the point is within the radius
                if(np.sqrt(i**2 + j**2) > radius):
                    continue
                x = sensor_data[0][0] + i
                y = sensor_data[0][1] + j
                if(x < 0 or x >= self.shape[1] or y < 0 or y >= self.shape[0]):
                    continue
                self.dissolved_oxygen_sensor_mask[y, x] = True
                self.dissolved_oxygen_sensor_layer[y, x] = sensor_data[1]
    
    def update_map(self):
        """
        Overlays sensor data onto the map image.
        Returns the updated map image.
        """
        self.map = self.map_image_layer.copy()
        # For sensor layer points that are not -inf, overlay colorjet
        self.map[self.dissolved_oxygen_sensor_mask] = cv2.applyColorMap(
            self.dissolved_oxygen_sensor_layer,
            cv2.COLORMAP_JET
        )[self.dissolved_oxygen_sensor_mask]
        return self.map
            

if __name__ == "__main__":
    # Example usage
    map_image = cv2.imread('map.jpg')  # Load a map image
    #test_sensor_image = cv2.imread('sensor_data.png')  # Load a map image
    asv_mapper = mapper(map_image)
    
    for i in range(300, 1200):
            # Simulate sensor data at random points
            sensor_data = ((i,500), np.random())  # Example sensor data at (i, 500) with value i % 255
            asv_mapper.update_dissolved_oxygen_layer(sensor_data, radius=3)
    # Update the map with sensor data
    updated_map = asv_mapper.update_map()
    
    # Display the updated map
    cv2.imshow('Updated Map', updated_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()