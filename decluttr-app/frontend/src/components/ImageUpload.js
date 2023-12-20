import React from 'react';

function ImageUpload({ onImageUpload }) {
  const handleFileChange = (event) => {
    if (event.target.files && event.target.files[0]) {
      onImageUpload(event.target.files[0]);
    }
  };

  return (
    <div className="flex justify-center p-4">
      <label className="block mb-2 text-sm font-medium text-black-900 dark:text-black-300">
        Select your photo
      </label>
      <input
        className="block w-1/3 text-sm text-gray-700 bg-gray-50 rounded-lg border border-gray-300 cursor-pointer focus:outline-none focus:border-gray-500"
        type="file"
        onChange={handleFileChange}
      />
    </div>
  );
}

export default ImageUpload;


 
  