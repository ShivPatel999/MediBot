const API_URL = 'http://localhost:8000/api';

export const chatWithMedibot = async (message) => {
    try {
        const response = await fetch(`${API_URL}/chat/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        if (!response.ok) throw new Error('Network response was not ok');
        return await response.json();
    } catch (error) {
        console.error("API Error:", error);
        throw error;
    }
};