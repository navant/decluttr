import React from 'react';

function ParamBoxes({ params, setParams }) {
  const handleChange = (event) => {
    const { name, value } = event.target;
    setParams(prev => ({ ...prev, [name]: value }));
  };

  return (
    <div className="flex flex-col items-center justify-center gap-4 p-4">
 <label className="block mb-2 text-sm font-medium text-black-900 dark:text-black-300">
Category     
 </label>
      <input
        type="text"
        name="category"
        value={params.category}
        onChange={handleChange}
        placeholder="Category"
        className="px-2 py-1 w-1/3 border rounded-lg text-gray-700 focus:outline-none focus:border-blue-500"
      />
       <label className="block mb-2 text-sm font-medium text-black-900 dark:text-black-300">
Sub Category     
 </label>
      <input
        type="text"
        name="subcategories"
        value={params.subcategories}
        onChange={handleChange}
        placeholder="Subcategories"
        className="px-2 py-1 w-1/3 border rounded-lg text-gray-700 focus:outline-none focus:border-blue-500"
      />
       <label className="block mb-2 text-sm font-medium text-black-900 dark:text-black-300">
Title     
 </label>
      <input
        type="text"
        name="title"
        value={params.title}
        onChange={handleChange}
        placeholder="Title"
        className="px-2 py-1 w-1/3 border rounded-lg text-gray-700 focus:outline-none focus:border-blue-500"
      />
       <label className="block mb-2 text-sm font-medium text-black-900 dark:text-black-300">
Description     
 </label>
      <textarea
        name="description"
        value={params.description}
        onChange={handleChange}
        placeholder="Description"
        className="px-2 py-1 w-1/3 border rounded-lg text-gray-700 focus:outline-none focus:border-blue-500"
      ></textarea>
       <label className="block mb-2 text-sm font-medium text-black-900 dark:text-black-300">
Condition     
 </label>
      <input
        type="text"
        name="condition"
        value={params.condition}
        onChange={handleChange}
        placeholder="Condition"
        className="px-2 py-1 w-1/3 border rounded-lg text-gray-700 focus:outline-none focus:border-blue-500"
      />
    </div>
  );
}

export default ParamBoxes;
