import React from 'react';

function GenerateButton({ onGenerate }) {
    return (
      <div className="flex justify-center py-2">
        <button
          onClick={onGenerate}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Generate
        </button>
      </div>
    );
  }
  
export default GenerateButton;

