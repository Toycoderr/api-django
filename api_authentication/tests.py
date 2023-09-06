from rest_framework.test import APITestCase
from authentication.models import CustomUser
from api_authentication.permissions import CustomUserPermission# Đảm bảo rằng bạn đã import CustomUser từ đúng module

class CustomUserPermissionTest(APITestCase):
    def setUp(self):
        # Tạo một người dùng để sử dụng trong bài kiểm tra
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

    def test_example(self):
        # Viết các bài kiểm tra của bạn ở đây
        pass
    
class CustomUserPermissionTest(APITestCase):
    def test_superuser_has_permission(self):
        # Tạo một superuser
        superuser = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123'
        )

        # Tạo một request object với user là superuser
        request = self.client.get('/some-url/')  # Thay đổi đường dẫn '/some-url/' thành đường dẫn thực tế của bạn
        request.user = superuser

        # Tạo một view object (giả sử là view cần kiểm tra permission)
        view = None  # Thay đổi view thành view cần kiểm tra

        # Tạo một instance của CustomUserPermission
        permission = CustomUserPermission()

        # Kiểm tra xem superuser có quyền không
        self.assertTrue(permission.has_permission(request, view))

    def test_non_superuser_does_not_have_permission(self):
        # Tạo một user thường
        user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

        # Tạo một request object với user là user thường
        request = self.client.get('/some-url/')  # Thay đổi đường dẫn '/some-url/' thành đường dẫn thực tế của bạn
        request.user = user

        # Tạo một view object (giả sử là view cần kiểm tra permission)
        view = None  # Thay đổi view thành view cần kiểm tra

        # Tạo một instance của CustomUserPermission
        permission = CustomUserPermission()

        # Kiểm tra xem user thường có quyền không
        self.assertFalse(permission.has_permission(request, view))