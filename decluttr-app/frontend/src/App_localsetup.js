// NOT USED - JUST LOCAL TEST
import React, { useState } from 'react';
import ImageUpload from './components/ImageUpload';
import ImagePreview from './components/ImagePreview';
import GenerateButton from './components/GenerateButton';
import ParamBoxes from './components/ParamBoxes';
import SubmitButton from './components/SubmitButton';
import ClearButton from './components/ClearButton';

function App() {
  const [image, setImage] = useState(null);
  const [previewUrl, setPreviewUrl] = useState('');
  const [params, setParams] = useState({ category: '', subcatergories: '', title: '' ,description:'',condition:''});


  const handleImageUpload = (file) => {
    setImage(file);
    setPreviewUrl(URL.createObjectURL(file));
  };

  const handleGenerate = async () => {
    if (!image) return;
  
    const reader = new FileReader();
    reader.readAsDataURL(image);
    reader.onloadend = async () => {
      let base64 = reader.result;
  
      // Strip off the data URI scheme prefix if it's present
      const base64WithoutPrefix = base64.split(',')[1] || base64;
  
      try {
        const response = await fetch('http://localhost:8000/api/item/describe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ image: base64WithoutPrefix }),
        });
        const data = await response.json();
        setParams(data);
      } catch (error) {
        console.error('Error:', error);
      }
    };
  };
  

  const handleSubmit = async () => {
    // Post API call to market URL
    const response = await fetch('YOUR_MARKET_ENDPOINT', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(params),
    });

    // Handle response from the market API
    // ...
  };

  const handleClear = () => {
    setImage(null);
    setPreviewUrl('');
    setParams({ x: '', y: '', description: '' });
  };

  return (
    <div className="bg-gray-100 text-gray-800 min-h-screen">
      <header className="text-center py-8">
        <h2 className="text-4xl font-semibold text-gray-700">Declutter your Personal items </h2>
      </header>

    <div  className="bg-gray-100 text-gray-800 min-h-screen">
      <ImageUpload onImageUpload={handleImageUpload} />
      {image && <ImagePreview src={previewUrl} />}
      <GenerateButton onGenerate={handleGenerate} />
      <ParamBoxes params={params} setParams={setParams} />
      <SubmitButton onSubmit={handleSubmit} />
      <ClearButton onClear={handleClear} />
    </div>
    </div>
  );
}

export default App;
