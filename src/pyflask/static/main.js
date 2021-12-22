function CheckFileSize(file, Size) {
    maxSize = Size * 1024 * 1024;
    if (file.files[0].size > maxSize) {
        alert("5MB 미만의 이미지만 업로드 가능합니다.");
        return false;
    }
    return true;
}
