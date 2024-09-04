import rosbag
import argparse

def rosbag_to_text(bagfile, output_file):
    with rosbag.Bag(bagfile, 'r') as bag, open(output_file, 'w') as f:
        for topic, msg, t in bag.read_messages():
            f.write(f"Time: {t.to_sec()} \nTopic: {topic} \nMessage: {msg}\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a ROS bag to a text file.")
    parser.add_argument("bagfile", help="Path to the input ROS bag file.")
    parser.add_argument("output_file", help="Path to the output text file.")
    
    args = parser.parse_args()

    rosbag_to_text(args.bagfile, args.output_file)
    print(f"Finished converting {args.bagfile} to {args.output_file}")
