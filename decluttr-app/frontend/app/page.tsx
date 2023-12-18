import Header from "@/app/components/header";
import ImageUpload from "./components/ImageUpload";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center gap-10 p-24 background-gradient">
      <Header />
      <ImageUpload />
    </main>
  );
}
