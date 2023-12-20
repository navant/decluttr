import React from 'react';

function SubmitButton({ onSubmit }) {
    return (
      <div className="text-center py-2">
        <button
          onClick={onSubmit}
          className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
        >
          Submit
        </button>
      </div>
    );
  }
  

export default SubmitButton;
