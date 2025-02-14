import { useState, useEffect, useRef } from "react";
import axios from "axios";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

interface Message {
  text: string;
  sender: "user" | "bot";
}

export const useChat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<null | HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async (userInput: string) => {
    if (!userInput.trim()) return;

    setMessages((prev) => [...prev, { text: userInput, sender: "user" }]);
    setLoading(true);

    try {
      const assignResponse = await axios.get(`${API_BASE_URL}/assign-task/`, {
        params: {
          user_id: "user_123",
          agent_name: "general_agent",
          user_input: userInput,
        },
      });

      const jobId = assignResponse.data.status;
      let result = null;

      while (!result) {
        await new Promise((resolve) => setTimeout(resolve, 2000));
        const jobResponse = await axios.get(`${API_BASE_URL}/job-result/`, {
          params: { job_id: jobId },
        });

        if (jobResponse.data.status === "completed") {
          result = jobResponse.data.result;
        }
      }

      setMessages((prev) => [...prev, { text: result, sender: "bot" }]);
    } catch (error) {
      console.error("Error fetching response:", error);
      setMessages((prev) => [
        ...prev,
        { text: "Error fetching response. Try again.", sender: "bot" },
      ]);
    }

    setLoading(false);
  };

  const resetChat = async () => {
    setLoading(true);
    try {
      const response = await axios.delete(`${API_BASE_URL}/reset-memory/`, {
        params: { user_id: "user_123" },
      });

      setMessages([]);
      return response.data.message || "Chat memory reset successfully.";
    } catch (error) {
      console.error("Error resetting chat memory:", error);
      throw new Error("Failed to reset memory. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return { messages, sendMessage, resetChat, loading, messagesEndRef };
};
