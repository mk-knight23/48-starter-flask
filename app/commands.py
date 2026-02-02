"""
Flask CLI Commands
"""
import click
from app import create_app
from app.models import db
from app.models.user import User, Post


app = create_app()


@app.cli.command()
def init_db():
    """Initialize the database"""
    db.create_all()
    click.echo('Database initialized.')


@app.cli.command()
def seed_db():
    """Seed database with sample data"""
    # Create admin user
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            email='admin@example.com',
            first_name='Admin',
            last_name='User',
            is_admin=True
        )
        admin.set_password('Admin123!')
        admin.save()
        click.echo('Admin user created.')
    
    # Create sample posts
    if Post.query.count() == 0:
        post1 = Post(
            title='Welcome to Flask Starter',
            content='This is your first blog post.',
            summary='Getting started with Flask',
            published=True,
            user_id=admin.id
        )
        post1.save()
        
        post2 = Post(
            title='API Documentation',
            content='Check out the API docs at /api/v1/docs',
            summary='API Documentation Guide',
            published=True,
            user_id=admin.id
        )
        post2.save()
        
        click.echo('Sample posts created.')
    
    click.echo('Database seeded successfully.')


@app.cli.command()
@click.option('--count', default=10, help='Number of users to create')
def create_users(count):
    """Create sample users"""
    from faker import Faker
    fake = Faker()
    
    for _ in range(count):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        user.set_password('Password123!')
        user.save()
    
    click.echo(f'{count} users created.')


@app.cli.command()
def reset_db():
    """Reset the database"""
    if click.confirm('Are you sure you want to reset the database?'):
        db.drop_all()
        db.create_all()
        click.echo('Database reset.')


@app.cli.command()
def routes():
    """List all routes"""
    from flask import current_app
    output = []
    
    for rule in current_app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods - {'HEAD', 'OPTIONS'}))
        output.append(f'{rule.endpoint:50s} {methods:20s} {rule.rule}')
    
    for line in sorted(output):
        click.echo(line)
