import React, { useState, useRef } from "react";
import ImageUpload from "./components/ImageUpload";
import ImagePreview from "./components/ImagePreview";
import GenerateButton from "./components/GenerateButton";
import ParamBoxes from "./components/ParamBoxes";
import SubmitButton from "./components/SubmitButton";
import ClearButton from "./components/ClearButton";

function App() {
  const [image, setImage] = useState(null);
  const [previewUrl, setPreviewUrl] = useState("");
  const [params, setParams] = useState({
    category: "",
    subcatergories: "",
    title: "",
    description: "",
    condition: "",
  });
  const fileInputRef = useRef(null);

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
      const base64WithoutPrefix = base64.split(",")[1] || base64;

      try {
        const response = await fetch(
          "http://localhost:8000/api/item/describe",
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              image: {
                data: base64WithoutPrefix,
                url: "", // Assuming the URL is not needed or blank in this case
              },
            }),
          }
        );
        const data = await response.json();

        if (data.item) {
          setParams({
            category: data.item.category,
            subcategories: data.item.subcategories,
            title: data.item.title,
            description: data.item.description,
            condition: data.item.condition,
          });
        } else {
          console.error("Error:", data.error_message);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    };
  };

  const handleSubmit = async () => {
    // Post API call to SUPABASE URL
    try {
      const response = await fetch("http://localhost:8000/api/item/record", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(params),
      });
      console.log("resonse", response);
    } catch (error) {
      console.log("Error:", error);
    }

    // Handle response from the market API
    // ...
  };

  const handleClear = () => {
    setImage(null); // Reset the image
    setPreviewUrl(""); // Reset the preview URL
    setParams({
      // Reset all parameters
      category: "",
      subcategories: [],
      title: "",
      description: "",
      condition: "",
    });
    if (fileInputRef.current) {
      fileInputRef.current.value = ""; // Reset the file input
    }
  };

  return (
    <div className="bg-gray-100 text-gray-800 min-h-screen">
      <header className="text-center py-8">
        <h2 className="text-4xl font-semibold text-gray-700">
          Declutter your Personal items{" "}
        </h2>
      </header>

      <div className="bg-gray-100 text-gray-800 min-h-screen">
        <ImageUpload onImageUpload={handleImageUpload} ref={fileInputRef} />
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
