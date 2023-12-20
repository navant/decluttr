import React from 'react';
function ClearButton({ onClear }) {
    return (
      <div className="text-center py-2">
        <button
          onClick={onClear}
          className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          Clear
        </button>
      </div>
    );
  }
  

export default ClearButton;
