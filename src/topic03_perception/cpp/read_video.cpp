#include "opencv2/opencv.hpp"

using namespace cv;

int main(int, char**)
{
    VideoCapture video_capture(2); // open the default camera
    if(!video_capture.isOpened())  // check if we succeeded
        return -1;

    Mat gray_image;
    namedWindow("edges",1);
    while(true)
    {
        Mat frame, frame_r;
        video_capture >> frame; // get a new frame from camera
        resize(frame, frame_r, Size(), 0.35, 0.35);
        cvtColor(frame_r, gray_image, COLOR_BGR2GRAY);
        //GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
        //Canny(edges, edges, 0, 30, 3);
        
        imshow("gray image", gray_image);
        if(waitKey(30) >= 0) break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}