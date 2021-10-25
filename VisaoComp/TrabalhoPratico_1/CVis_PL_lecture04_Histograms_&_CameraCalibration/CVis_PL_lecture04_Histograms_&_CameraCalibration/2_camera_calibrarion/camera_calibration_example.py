import numpy as np
import cv2
import glob

#############################################################################################################
# General options
#############################################################################################################
chessboardSize = (24,17)
frameSize = (1440,1080)


# termination criteria for cornerSubPix()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


images = glob.glob('*.png')

for fname in images:

    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    # https://docs.opencv.org/master/d9/d0c/group__calib3d.html#gad0e88e13cd3d410870a99927510d7f91
    ret, corners = cv2.findChessboardCorners(gray, chessboardSize, None)

    # If found, add object points, image points (after refining them)
    if ret is True:

        objpoints.append(objp)
        # https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#ga354e0d7c86d0d9da75de9b9701a9a87e
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria) #  Refines the corner locations
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, chessboardSize, corners2, ret)
        cv2.imshow(fname, img)
        cv2.waitKey(1000)

cv2.destroyAllWindows()

#  Calibrate the camera

#  https://docs.opencv.org/3.4.15/d9/d0c/group__calib3d.html#ga687a1ab946686f0d85ae0363b5af1d7b
#  returns the camera matrix, distortion coefficients, rotation and translation vectors etc.
ret, cameraMatrix, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, frameSize, None, None)


# Image undistortion: 2 methods, the same result

img = cv2.imread('test_sample.jpg')
h,  w = img.shape[:2]
#  https://docs.opencv.org/3.4.15/d9/d0c/group__calib3d.html#ga7a6c4e032c97f03ba747966e6ad862b1
#  retval, validPixROI = cv.getOptimalNewCameraMatrix(cameraMatrix, distCoeffs, imageSize, alpha, newImgSize, centerPrincipalPoint)
newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))
print(newCameraMatrix) #  can be saved for future usage

# Undistort function
dst = cv2.undistort(img, cameraMatrix, dist, None, newCameraMatrix)

# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
#  cv2.imwrite('caliResult1.jpg', dst)
cv2.imshow('caliResult1.jpg', dst)
  
# Undistort with Remapping
mapx, mapy = cv2.initUndistortRectifyMap(cameraMatrix, dist, None, newCameraMatrix, (w,h), 5)
dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
#  cv2.imwrite('caliResult2.jpg', dst)
cv2.imshow('caliResult2.jpg', dst)

# Reprojection Error
mean_error = 0

for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], cameraMatrix, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    mean_error += error

print( "total error: {}".format(mean_error/len(objpoints)) )
