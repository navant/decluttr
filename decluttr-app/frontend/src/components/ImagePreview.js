import React from 'react';

function ImagePreview({ src }) {
    return (
      <div className="flex justify-center p-4">
        <img src={src} alt="Preview" className="rounded-lg shadow-lg max-w-full h-auto align-middle border-none" />
      </div>
    );
  }
  

export default ImagePreview;
