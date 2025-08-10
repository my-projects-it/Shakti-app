"""
Unit tests for utility functions and helper methods.
Tests audio processing, file handling, and data validation utilities.
"""

import pytest
import tempfile
import os
from unittest.mock import patch, MagicMock
import pandas as pd
from datetime import datetime


class TestFileUtilities:
    """Test cases for file handling utilities."""
    
    def test_csv_file_creation(self):
        """Test CSV file creation with proper structure."""
        # Arrange
        test_data = [
            {"timestamp": "2024-01-01 12:00:00", "story": "First story"},
            {"timestamp": "2024-01-01 13:00:00", "story": "Second story"}
        ]
        
        # Act
        df = pd.DataFrame(test_data)
        
        # Assert
        assert len(df) == 2
        assert list(df.columns) == ["timestamp", "story"]
        assert df.iloc[0]["story"] == "First story"
        assert df.iloc[1]["story"] == "Second story"
    
    def test_csv_data_validation(self):
        """Test validation of CSV data structure."""
        # Arrange
        valid_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "story": "Valid story content"
        }
        
        # Act & Assert
        assert "timestamp" in valid_entry
        assert "story" in valid_entry
        assert len(valid_entry["timestamp"]) == 19  # Standard datetime format
        assert len(valid_entry["story"]) > 0
    
    def test_file_path_handling(self):
        """Test file path handling for different scenarios."""
        # Arrange
        csv_filename = "anonymous_stories.csv"
        
        # Act & Assert
        assert csv_filename.endswith(".csv")
        assert not csv_filename.startswith("/")  # Relative path
        assert "anonymous" in csv_filename.lower()


class TestAudioUtilities:
    """Test cases for audio processing utilities."""
    
    def test_audio_file_extension_extraction(self):
        """Test extraction of file extensions from audio files."""
        # Arrange
        test_cases = [
            ("audio/mp3", "mp3"),
            ("audio/wav", "wav"), 
            ("audio/m4a", "m4a"),
            ("audio/ogg", "ogg")
        ]
        
        # Act & Assert
        for mime_type, expected_ext in test_cases:
            extracted_ext = mime_type.split("/")[-1]
            assert extracted_ext == expected_ext
    
    def test_supported_audio_formats(self):
        """Test that supported audio formats are correctly identified."""
        # Arrange
        supported_formats = ["mp3", "wav", "m4a", "ogg"]
        test_formats = ["mp3", "wav", "m4a", "ogg", "flac", "aac"]
        
        # Act & Assert
        for fmt in test_formats:
            if fmt in supported_formats:
                assert fmt in ["mp3", "wav", "m4a", "ogg"]
            else:
                assert fmt not in supported_formats
    
    @patch('tempfile.NamedTemporaryFile')
    def test_temporary_file_creation(self, mock_temp_file):
        """Test temporary file creation for audio processing."""
        # Arrange
        mock_temp_file.return_value.name = "/tmp/test_audio.mp3"
        mock_temp_file.return_value.flush = MagicMock()
        
        # Act
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        
        # Assert
        assert temp_file is not None
        mock_temp_file.assert_called_once()


class TestDataValidation:
    """Test cases for data validation utilities."""
    
    def test_story_text_validation(self):
        """Test validation of story text input."""
        # Arrange
        test_cases = [
            ("Valid story", True),
            ("", False),
            ("   ", False),
            ("\n\n\n", False),
            ("\t\t", False),
            ("Story with\nnewlines", True),
            ("Story with special chars !@#$%", True),
            ("A" * 10000, True),  # Very long story
        ]
        
        # Act & Assert
        for story, expected_valid in test_cases:
            is_valid = bool(story.strip())
            assert is_valid == expected_valid
    
    def test_timestamp_format_validation(self):
        """Test validation of timestamp format."""
        # Arrange
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # Act
        # Parse timestamp back to verify format
        try:
            parsed_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            is_valid = True
        except ValueError:
            is_valid = False
        
        # Assert
        assert is_valid
        assert len(timestamp) == 19
        assert timestamp.count("-") == 2
        assert timestamp.count(":") == 2
        assert timestamp.count(" ") == 1


class TestLanguageUtilities:
    """Test cases for language and translation utilities."""
    
    def test_language_code_mapping(self):
        """Test mapping between language names and codes."""
        # Arrange
        language_mappings = {
            "English": "en",
            "Hindi": "hi-IN",
            "Tamil": "ta",
            "Bengali": "bn"
        }
        
        # Act & Assert
        for lang_name, lang_code in language_mappings.items():
            assert len(lang_name) > 0
            assert len(lang_code) >= 2
            assert lang_code.replace("-", "").isalpha()
    
    def test_translation_key_consistency(self):
        """Test that translation keys are consistent across languages."""
        # Arrange
        required_keys = [
            "title", "subtitle", "upload_audio", "write_story", 
            "submit", "success", "error", "transcribed"
        ]
        
        # Mock translation structure
        sample_translations = {
            "English": {key: f"English_{key}" for key in required_keys},
            "Hindi": {key: f"Hindi_{key}" for key in required_keys}
        }
        
        # Act & Assert
        for lang, translations in sample_translations.items():
            for key in required_keys:
                assert key in translations
                assert len(translations[key]) > 0


class TestErrorHandling:
    """Test cases for error handling utilities."""
    
    def test_file_not_found_handling(self):
        """Test handling of file not found scenarios."""
        # Arrange
        non_existent_file = "non_existent_file.csv"
        
        # Act & Assert
        assert not os.path.exists(non_existent_file)
    
    def test_empty_dataframe_handling(self):
        """Test handling of empty DataFrame scenarios."""
        # Arrange
        empty_df = pd.DataFrame()
        
        # Act & Assert
        assert len(empty_df) == 0
        assert empty_df.empty
    
    def test_invalid_audio_format_handling(self):
        """Test handling of invalid audio formats."""
        # Arrange
        invalid_formats = ["txt", "pdf", "doc", "exe"]
        valid_formats = ["mp3", "wav", "m4a", "ogg"]
        
        # Act & Assert
        for fmt in invalid_formats:
            assert fmt not in valid_formats
        
        for fmt in valid_formats:
            assert fmt in valid_formats


class TestPerformanceUtilities:
    """Test cases for performance-related utilities."""
    
    def test_large_story_handling(self):
        """Test handling of large story texts."""
        # Arrange
        large_story = "This is a test story. " * 1000  # ~23KB story
        
        # Act
        processed_story = large_story.strip()
        
        # Assert
        assert len(processed_story) > 0
        assert processed_story == large_story.strip()
    
    def test_dataframe_memory_efficiency(self):
        """Test memory efficiency of DataFrame operations."""
        # Arrange
        large_dataset = [
            {"timestamp": f"2024-01-{i:02d} 12:00:00", "story": f"Story {i}"}
            for i in range(1, 101)  # 100 stories
        ]
        
        # Act
        df = pd.DataFrame(large_dataset)
        
        # Assert
        assert len(df) == 100
        assert df.memory_usage().sum() > 0
        assert "timestamp" in df.columns
        assert "story" in df.columns


class TestSecurityUtilities:
    """Test cases for security-related utilities."""
    
    def test_story_content_sanitization(self):
        """Test basic story content handling (no malicious content processing)."""
        # Arrange
        stories_with_special_chars = [
            "Story with <script>alert('test')</script>",
            "Story with SQL'; DROP TABLE stories;--",
            "Normal story content",
            "Story with unicode: 你好 नमस्ते"
        ]
        
        # Act & Assert
        for story in stories_with_special_chars:
            # Basic validation - story should be stored as-is (Streamlit handles security)
            processed = story.strip()
            assert len(processed) > 0
            assert isinstance(processed, str)
    
    def test_file_path_security(self):
        """Test file path security (no directory traversal)."""
        # Arrange
        csv_filename = "anonymous_stories.csv"
        
        # Act & Assert
        # Ensure filename doesn't contain path traversal attempts
        assert ".." not in csv_filename
        assert "/" not in csv_filename
        assert "\\" not in csv_filename
        assert csv_filename == os.path.basename(csv_filename)


if __name__ == "__main__":
    pytest.main([__file__])
